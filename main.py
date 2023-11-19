# my_main.py
# ...the backend of our application...
''' This script launches processes '''
from database_utils import DatabaseConnector
from data_extraction  import DataExtractor
from data_cleaning import DataCleaner

import sys 
print(sys.version_info)

# Extract, Transform and Load: table: "card_details", from pdf file to postgres 'sales_data' db, 
def run_card_details_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    raw_card_details = extractor.fetch_pdf_data()
    print(type(raw_card_details))#<class 'pandas.core.frame.DataFrame'>
    clean_card_details = cleaner.clean_card_data(raw_card_details)
    #breakpoint()
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('card_details',clean_card_details,target_creds)

# Extract, Transfer and Load: table: "data_times", from json file to postgres's db, 
def run_data_times_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    raw_data_times = extractor.fetch_json_data()
    print(type(raw_data_times))
    #breakpoint()
    clean_data_times = cleaner.clean_data_times(raw_data_times)
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('data_times',clean_data_times,target_creds)

# Extract, Transfer and Load: table: "orders_table", from xxxx to postgres's db, 
def run_orders_table_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    source_creds = connector.read_db_creds('source_creds.yaml')
    source_engine = connector.init_db_engine(source_creds)
    orders_table = extractor.read_rds_table(source_engine)
    clean_orders_table = cleaner.clean_orders_data(orders_table)
    print(type(clean_orders_table))
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('orders_table',clean_orders_table,target_creds)

# Extract, Transfer and Load: table: "stores_table",
def run_stores_table_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    store_df = extractor.list_retrieve_stores()
    clean_stores_table = cleaner.clean_stores_data(store_df)
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('stores_table',clean_stores_table,target_creds)

#Extract, Transfer and Load: table: "products_table",
def run_products_table_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    products_df = extractor.extract_from_s3()
    clean_products = cleaner.clean_products_data(products_df)
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('products_table',clean_products,target_creds)

# Extract, Transfer and Load: table: "users_table", from xxxx to postgres's db,
def run_users_table_pipeline():
    extractor = DataExtractor()
    cleaner = DataCleaner()
    connector = DatabaseConnector()
    source_creds = connector.read_db_creds('source_creds.yaml')
    source_engine = connector.init_db_engine(source_creds)
    users_table = extractor.read_rds_table_2(source_engine)
    clean_users_table = cleaner.clean_users_data(users_table)
    target_creds = connector.read_db_creds('target_creds.yaml')
    connector.init_db_engine(target_creds)
    connector.upload_to_db('users_table',clean_users_table,target_creds)


# run pipeline for each table , instantiating the class ... 
if __name__ == "__main__":
    run_card_details_pipeline()
    run_data_times_pipeline()
    run_orders_table_pipeline()
    run_stores_table_pipeline()
    run_products_table_pipeline()
    run_users_table_pipeline()
    #