import pandas as pd
import os
from sqlalchemy import create_engine
# Imports the create_engine function from the SQLAlchemy library so you can connect your Python program to a database.abs

import logging                 #standrad lib for storing the logs
import time                      #for keeping record of time

logging.basicConfig(
    filename="logs/ingestion_db.log",                      #where these logs are stored
    level=logging.DEBUG,                    #type of log(debug, error, info, )
    format="%(asctime)s - %(levelname)s - %(message)s",         #log store format 
    filemode="a"            #append after the existing log
)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    ''' This function will ingest the dataframe into database table'''
    df.to_sql(table_name, con=engine, if_exists = 'replace', index = False)
    # ingest_db() saves a Pandas DataFrame into a SQL database table using a SQLAlchemy database connection.

def load_raw_data():
    ''' This function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):   #it brings all the file from data folder
        if '.csv' in file:            #it filters only the file which contains .csv
            print(file)
            df = pd.read_csv('data/'+file)             #it creates data frame from .csv file
            logging.info(f'Ingesting {file} in db')                   #gives shape of file (row, col)
            ingest_db(df, file[:-4], engine)   #file[:-4] removes .csv from last and give database name same as file name       
    end = time.time()
    total_time = (end-start)/60
    logging.info('Ingestion Complete')
    logging.info(f'Total time taken: {total_time} minutes')

if __name__ == '__main__':
    load_raw_data()