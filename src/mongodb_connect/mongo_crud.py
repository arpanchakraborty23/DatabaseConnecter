from typing import Any
import os
import pandas as pd
import numpy as np
import pymongo
import json
from ensure import ensure_annotations

from pymongo.mongo_client import MongoClient
from ensure import ensure_annotations

class mogo_oparation:
    __colloection=None # here i have created a private/protected variable
    __database=None


    def __init__(self,client_url:str,database_name:str,collection_name:str):
            self.client_url=client_url
            self.database_name=database_name
            self.collection_name=collection_name

    def created_mongo_client(self,collection=None):
            client=MongoClient(self.client_url)
            return client

    def create_database(self,collection=None):
            if mongo_oparation.__database==None:
                client=self.created_mongo_client(collection)
                self.database=client[self.database]
                return self.database  

    def create_collection(self,collection=None):   
            if mongo_oparation.__colloection==None:
                database=self.create_database(collection)
                self.collection=database[self.collection_name]
                mongo_oparation.__colloection=collection

            if mongo_oparation.__colloection!=collection:
                database_name=self.create_database(collection)
                self.collection=database[self.collection_name]
                mogo_oparation.__colloection=collection

            return self.collection

    def insert_record(self,record:dict,collection_name:str)->Any:
                if type(record)==list:
                    for data in record:
                        if type(data)!=dict:
                            raise TabError('Record must be Dict')

                    collection=self.create_collection(collection_name)
                    collection.insert_many(record)

                elif type(record)==dict:
                    collection=self.create_collection(collection_name)
                    collection.insert_one(record)

    def bulk_insert(self,data_file,collection_name:str=None):
        self.path=data_file

        if self.path.endswith('.csv'):
            pd.read_csv(self.path,encoding='utf-8')

        elif self.path.endswith('.xlsx'):
            dataframe=pd.read_csv(self.path,encoding='utf-8')

            datajson=json.loads(dataframe.to_json(orient='record'))
            collection=self.create_collection()
            collection.insert_many(datajson)                    

