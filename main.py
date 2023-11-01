from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.pipeline.exception import SensorException
from sensor.pipeline.logger import logging
import os,sys

def test_Exception():
    try:
        logging.info("we are dividing a number by zero.")
        x=1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__ == '__main__':

    try:
        test_Exception()
    except Exception as e:
        print(e)

    

    mongodb_client = MongoDBClient()
    print("collection name:",mongodb_client.database.list_collection_names())