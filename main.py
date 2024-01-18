from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.exception import SensorException
from sensor.pipeline.logger import logging
import os,sys
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

if __name__ == '__main__':
    training_pipeline_config=TrainingPipelineConfig()
    dat_ingestion_config=DataIngestionConfig(training_pipeline_config)
    print(dat_ingestion_config.__dict__)

