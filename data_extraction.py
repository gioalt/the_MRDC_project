# data_extraction.py
# class DataExtractor()
# this class contains methods for collecting specific data resource types;
# it makes use of various python modules/packages 
#
# import required packages
import pandas as pd
import numpy as np
import json
import requests
#import sqlalchemy as sa
#from sqlalchemy import create_engine
from tabula import read_pdf
import requests
import boto3
import yaml
#
#
#
class DataExtractor:
	''' This class create data (from various source) in sql'''
	#return pd.read_sql_table(table_name, engine)# engine = 
	def read_rds_table(self,engine):
		orders_table = pd.read_sql_table('orders_table', engine)
		print(orders_table.head())
		return orders_table
    
	def read_rds_table_2(self,engine):
		orders_table = pd.read_sql_table('legacy_users', engine)
		print(orders_table.head())
		return orders_table

     # method read date times from json  
	def fetch_json_data(self):
		#data_times = pd.read_json("data_details.json")
		src = " https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json"
		data_times = pd.read_json(src)
		return data_times
	
	# here any other data-type-import method, for ex. pdf
	def fetch_pdf_data(self):
		src = "https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf"
		df = read_pdf(src,stream=False,pages="all")# changed from True to False
		data = pd.concat(df,ignore_index=True)
		card_details = pd.DataFrame(data)
		print(card_details.head())#
		print(card_details.shape)# how many rows and columns? False (15309, 4),True (15309, 6)
		return card_details

	def API_key(self):
		file_api = 'x_api_key.yaml'
		with open(file_api, 'r') as api_key:
			headers = yaml.safe_load(api_key)
		x_api_key = headers['headers']
		return x_api_key

	#def list_number_of_stores():
	def list_number_of_stores(self):
		api_url_base = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
		response = requests.get(api_url_base,headers=self.API_key())
		print('Response status code:', response.status_code)#200
		print(response.json()['number_stores'])#451
		return response.json()['number_stores']
	#
	def list_retrieve_stores(self):
		#api_url_base = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
		api_url_base = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details'
		store = self.list_number_of_stores()
		list_of_stores = []
		for idx,store in enumerate(range(store)):
			store_number = requests.get(f'{api_url_base}/{idx}',headers = self.API_key())
			#print(idx, store_number.json())
			store_number_df = pd.DataFrame(store_number.json(),index=[np.NaN])
			list_of_stores.append(store_number_df)
		store_df = pd.concat(list_of_stores)
		return store_df

	def extract_from_s3(self):
		s3_client = boto3.client("s3")
		response = s3_client.get_object(Bucket='data-handling-public', Key='products.csv')
		status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")
		print(status)
		print(type(response))#dictionary<class 'dict'>
		products_df = pd.read_csv(response.get("Body"))#<class 'pandas.core.frame.DataFrame'>
		print(type(products_df))
		print(products_df.shape)#(1853, 10)
		print(products_df.head())
		return products_df


# if __name__ == "__main__":
# 	datax = DataExtractor()# create an object of class
# 	print(datax)# <__main__.DataExtractor object at 0x100a20110>
# 	experiment = datax.extract_from_s3()
# 	experiment.to_csv('experiment3.csv')
# TEST NEW API KEY FEED: PASS; comment below lines out
if __name__ == "__main__":
	datax = DataExtractor()
	experiment = datax.API_key()
	print(experiment)
	experiment_2 = datax.list_retrieve_stores()
	print(experiment_2)