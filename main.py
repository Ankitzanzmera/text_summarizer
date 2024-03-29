import sys
from text_summarizer.utils.logger import logger
from text_summarizer.utils.exception import CustomException
from text_summarizer.pipelines.pipeline_01_data_ingestion import DataIngestionPipeline
from text_summarizer.pipelines.pipeline_02_data_validation import DataValidationPipeline
from text_summarizer.pipelines.pipeline_03_data_transformation import DataTransformationPipeline
from text_summarizer.pipelines.pipeline_04_model_trainer import ModelTrainerPipeline
from text_summarizer.pipelines.pipeline_05_model_evaluation import ModelEvaluationPipeline

# STAGE_NAME = "Data_Ingestion"
# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
#         obj = DataIngestionPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
#         logger.info("-"*70)
#     except Exception as e:
#         raise CustomException(e,sys)

# STAGE_NAME = "Data Validation"
# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
#         obj = DataValidationPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
#         logger.info("-"*70)
#     except Exception as e:
#         raise CustomException(e,sys)
    
# STAGE_NAME = "Data Transformation"

# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
#         obj = DataTransformationPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
#         logger.info("-"*70)
#     except Exception as e:
#         raise CustomException(e,sys)

# STAGE_NAME = "Model Trainer"
# if __name__ == "__main__":
#     try:
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
#         obj = ModelTrainerPipeline()
#         obj.main()
#         logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
#         logger.info("-"*70)
#     except Exception as e:
#         raise CustomException(e,sys)

STAGE_NAME = "Model Evaluation"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Started <<<<<<<<<<<<<<<<<<<<<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>>>>>>>>>>>>>>>>>>>> {STAGE_NAME} Completed <<<<<<<<<<<<<<<<<<<<<<<<<")
        logger.info("-"*70)
    except Exception as e:
        raise CustomException(e,sys)