# my_data_cleaning.py
# methods to clean each data resource
# make use of python pandas
import pandas as pd

class DataCleaner:
    ''' This class cleans data in various ways ... '''
    # method that cleans orders table (retrieved from  S3 AWS)
    def clean_orders_data(self,orders_table):
        duplicate_rows = orders_table.duplicated()
        print("Number of duplicate rows (orders table):", duplicate_rows.sum())# no: 0
        clean_orders_table = orders_table.drop(['first_name','last_name','1'],axis = 1)
        print(clean_orders_table)
        return clean_orders_table
    
    # method that cleans data times (retrieved from json)
    def clean_data_times(self,data_times):
        duplicate_rows = data_times.duplicated()
        print("Number of duplicate rows (data times):", duplicate_rows.sum())#no: 14
        #date_times = date_times.drop_duplicates(inplace=True)
        print(type(data_times.drop_duplicates(inplace=True)))
        data_times = pd.DataFrame(data_times)
        print(type(data_times))
        print(data_times.head())
        return data_times
    
    # clean the pdf data from and go to utils to push it to the target db
    def clean_card_data(self,card_details):
        duplicate_rows = card_details.duplicated()
        print("Number of duplicate rows (card data):", duplicate_rows.sum())# no: 9
        #clean_card_details = card_details.drop_duplicates(inplace=True)# changes original dataframe!
        clean_card_details = card_details.drop_duplicates(inplace=False)# 
        print(type(clean_card_details))
        #print(clean_card_details.head())
        return clean_card_details
    
    # clean the store df like the others
    def clean_stores_data(self,stores_df):
        selection = ['GB','US','DE']
        stores_df2 = stores_df[stores_df.country_code.isin(selection)]
        #store_df.loc[:,'country_code'] = store_df.loc[store_df['country_code'].isin(selection)]
        print(stores_df2.shape)
        #duplicate_rows = store_df.duplicated()
        #print("Number of duplicate rows:", duplicate_rows.sum())# no:0
        #clean_stores_table = store_df.drop_duplicates(inplace=False)
        clean_stores_table = stores_df2
        print(clean_stores_table.shape)
        return clean_stores_table
        # there are three rows with NULL in all columns
        # there are mispelled categories in Country
        # latiitude is poorly populated
        # there iis nothing at index 0 ...
        # line 447 it s all funny
        # all in pandas

    def convert_product_weights(self, products_df):
        pass
    
    def clean_products_data(self,products_df):
        products_df.dropna(how='any',inplace= True)
        products_df.reset_index(inplace=True)  
        print(products_df.shape)#(1849, 11)
        return products_df
    
    def clean_users_data(self,users_table):
        print("Number of rows and columns:", users_table.shape)# it does not come out!
        users_table = users_table.dropna(axis=0,how='any')
        duplicate_rows = users_table.duplicated()
        print("Number of duplicate rows  (users data):", duplicate_rows.sum())# no: 0
        clean_users_table = users_table.copy()
        print(clean_users_table.shape)
        #clean_users_table = users_table.drop(['first_name','last_name','1'],axis = 1)
        print(clean_users_table)
        return clean_users_table


# if __name__ == "__main__":
# 	datax = DataCleaner()# create an object of class
# 	print(datax)# <__main__.DataExtractor object at 0x100a20110>
# 	experiment = datax.clean_stores_data(stores_df)
# 	experiment.to_csv('experiment_8.csv')


