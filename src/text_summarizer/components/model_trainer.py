import os,sys
import torch
from transformers import DataCollatorForSeq2Seq
from datasets import load_dataset,load_from_disk
from transformers import TrainingArguments, Trainer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from text_summarizer.utils.exception import CustomException
from text_summarizer.utils.logger import logger
from text_summarizer.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self,config:ModelTrainerConfig):
        self.config = config

    def train(self):
        try:
            device = "cuda" if torch.cuda.is_available() else "cpu"
            tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
            model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
            seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer,model = model_pegasus)

            # Loading Dataset
            dataset_samsum_pt = load_from_disk(self.config.transformed_data_path)
            
            # training_args = TrainingArguments(
            #     output_dir = self.config.root_dir,
            #     num_train_epochs = self.config.num_train_epochs,
            #     warmup_steps = self.config.warmup_steps,
            #     per_device_train_batch_size = self.config.per_device_train_batch_size,
            #     per_device_eval_batch_size = self.config.per_device_train_batch_size,
            #     weight_decay = self.config.weight_decay,
            #     logging_steps = self.config.logging_steps,
            #     evaluation_strategy = self.config.evaluation_strategy,
            #     eval_steps = self.config.eval_steps,
            #     save_steps = self.config.save_steps,
            #     gradient_accumulation_steps = self.config.gradient_accumulation_steps
            # )
            
            training_args = TrainingArguments(
            output_dir=self.config.root_dir, num_train_epochs=1, warmup_steps=500,
            per_device_train_batch_size=1, per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, save_steps=1e6,
            gradient_accumulation_steps=16
        ) 

            trainer = Trainer(model = model_pegasus,
                            args = training_args,
                            tokenizer = tokenizer,
                            data_collator = seq2seq_data_collator,
                            train_dataset = dataset_samsum_pt['test'],
                            eval_dataset = dataset_samsum_pt['validation']
                            )
            
            trainer.train()
            logger.info("Training Has Completed")

            ## Save Model
            model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus_samsum_model"))

            ## Save Tokenizer
            tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
            logger.info("Model and Tokenizer has been Saved...")
        except Exception as e:
            raise CustomException(e,sys)