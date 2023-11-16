# database_utils.py
# class DatabaseConnector()
# this method enables to connect to postgreSQL database: sales_data
#  it makes use of various python modules/packages including SQLAlchemy for connection
# first to be built
import yaml
import psycopg2
import sqlalchemy as sa
from sqlalchemy import create_engine
import requests
#
#
class DatabaseConnector:
    ''' This class reads credentials, sets up connection engines, and inspects data '''
    # method reads and returns source db credentials for engine creation
    def read_db_creds(self,file_creds):
        with open(file_creds, 'r') as creds:
                database_creds = yaml.safe_load(creds)
                print(database_creds)
                return database_creds
    
    # method sets up a connection to the source database using db credentials
    def init_db_engine(self,creds):
        engine = sa.create_engine(f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}")
        return engine
    
    # method to list the table in the engine: inspect
    def list_db_tables(self, engine):
        inspector = sa.inspect(engine)
        list_of_tables = inspector.get_table_names()
        print(list_of_tables)# in case you want to select a specific table,
        return list_of_tables
        #['legacy_store_details', 'legacy_users', 'orders_table']
    
    # method to push tables to target dataframe.to_sql()
    def upload_to_db(self,table_to_upload,dataframe,creds):
        #date_times.to_sql(date_times, target_engine, index=False, if_exists='replace')
        #return date_times.to_sql(date_times, target_engine, index=False, if_exists='replace')
        return dataframe.to_sql(table_to_upload, self.init_db_engine(creds), index=False, if_exists='replace')