import os, sys

from thyroid.logger import logging
from thyroid.exception import ThyroidException
from thyroid.utils import get_collection_as_dataframe

from thyroid.entity import config_entity, artifact_entity
from thyroid.entity.config_entity import DataIngestionConfig
from thyroid.entity.config_entity import DataValidationConfig
from thyroid.entity.config_entity import DataTransformationConfig

from thyroid.components.data_ingestion import DataIngestion
from thyroid.components.data_validation import DataValidation
from thyroid.components.model_pusher import ModelPusher
from thyroid.components.data_transformation import DataTransformation
from thyroid.components.model_trainer import ModelTrainer
from thyroid.components.model_evaluation import ModelEvaluation





def start_training_pipeline():
    try:
         training_pipeline_config = config_entity.TrainingPipelineConfig()

         #data ingestion         
         data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
         print(data_ingestion_config.to_dict())
         data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
         data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    except Exception as e:
        raise ThyroidException(e,sys)