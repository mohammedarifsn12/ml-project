import os
import sys
from src import exception
from src.components import data_transformation
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig

from src.components.model_trainer import modeltrainer
from src.components.model_trainer import modeltrainerconfig
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method')
        try:
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('reading the dataset as as dataframe')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.20,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('ingestion of data is completed')
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except exception as e:
            raise CustomException(e,sys)


if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation_new=DataTransformation()
    train_arr,test_arr,_=data_transformation_new.initiate_data_transformation(train_data,test_data)
    modeltrainernew=modeltrainer()
    print(modeltrainernew.initiate_model_trainer(train_arr,test_arr))