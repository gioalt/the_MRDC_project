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
        selection = ['Evening','Late_Hours','Midday','Morning']
        data_times = data_times[data_times.time_period.isin(selection)]
        print(type(data_times))
        print(data_times.head())
        return data_times
    
    # clean the pdf data from and go to utils to push it to the target db
    def clean_card_data(self,card_details):
        print(card_details.shape)
        print(card_details.head())
        #duplicate_rows = card_details.duplicated()
        #print("Number of duplicate rows (card data):", duplicate_rows.sum())# no: 10
        #clean_card_details = card_details.drop_duplicates(inplace=True)# changes original dataframe!
        clean_card_details = card_details.drop_duplicates(inplace=False)# 
        print(type(clean_card_details))
        print(clean_card_details.shape)
        clean_card_details['card_number'] = clean_card_details['card_number'].astype('string')
        clean_card_details['card_number'] = clean_card_details['card_number'].str.replace('?','')
        #unwanted_rows =['Z8855EXTJX','Y8ITI33X30','VAB9DSB8ZM','T23BTBBJDD','RNSCD8OCIM','OMZSBN2XG3','NULL','NB8JJ05D7R','MOZOT5Q95V','MIK9G2EMM0','LSWT9DT4G4','K0084A9R99','JQTLQAAQTD','I4PWLWSIRJ','G0EF4TS8C8']
        #result = clean_card_details.drop(unwanted_rows,axis=1)
        #result = clean_card_details['card_number'].isalnum()
        #result = clean_card_details['card_number'].isinstance('card_number',float)
        print(clean_card_details.shape)
        card_details.to_csv("test2_card_details.csv")
        cards_selection = ['American Express','Diners Club /Carte Blanche','Discover','JCB 15 digit','JCB 16 digit','Maestro','Mastercard','VISA 13 digit','VISA 16 digit','VISA 19 digit']
        clean_card_details = clean_card_details[clean_card_details.card_provider.isin(cards_selection)]
        print(clean_card_details.shape)
        print(type(clean_card_details['card_number']))
        #clean_card_details.dropna(how='any',inplace=True)
        #print(clean_card_details.head())
        return clean_card_details
    
    # clean the store df like the others
    def clean_stores_data(self,stores_df):
        print(stores_df.shape)
        stores_df = stores_df.drop(['lat'],axis = 1)
        duplicate_rows = stores_df.duplicated()
        selection = ['US','GB','DE']
        stores_df = stores_df[stores_df.country_code.isin(selection)]
        print("Number of duplicate rows:", duplicate_rows.sum())# no:0
        clean_stores_table= stores_df.drop_duplicates(inplace=False)
        print(clean_stores_table.shape)
        return clean_stores_table
        #clean_stores_table = stores_table.drop(['lat'],axis = 1)
        # there are three rows with NULL in all columns
        # there are mispelled categories in Country
        # latiitude is poorly populated
        # there iis nothing at index 0 ...
        # line 447 it s all funny
        # all in pandas
    
    def clean_products_data(self,products_df):
        print(products_df.shape)# (xxxxx, 11)
        products_df.dropna(how='any',inplace= True)
        products_df.reset_index(inplace=True)
        selection = ['diy','food-and-drink','health-and-beauty','homeware','pets','sports-andd-leisure','toys-and-games']
        products_df = products_df[products_df.category.isin(selection)]
        print(products_df.shape)# (1806, 11)
        print(products_df.head())
        # £ -> '' str -> float
        products_df['product_price'] = products_df['product_price'].astype('string')
        products_df['product_price'] = products_df['product_price'].str.replace('£','')
        products_df['product_price']= products_df['product_price'].astype(float)
        
        ##### to do
        
        #####
        
        return products_df

        
    
    def clean_users_data(self,users_table):
        print("Number of rows and columns:", users_table.shape)# it does not come out!
        users_table = users_table.dropna(axis=0,how='any')
        duplicate_rows = users_table.duplicated()
        print("Number of duplicate rows  (users data):", duplicate_rows.sum())# no: 0
        clean_users_table = users_table.copy()
        selection = ['US','GB','DE']
        clean_users_table = clean_users_table[clean_users_table.country_code.isin(selection)]
        print(clean_users_table.shape)
        #clean_users_table = users_table.drop(['first_name','last_name','1'],axis = 1)
        print(clean_users_table)
        return clean_users_table


# if __name__ == "__main__":
# 	datax = DataCleaner()# create an object of class
# 	print(datax)# <__main__.DataExtractor object at 0x100a20110>
# 	experiment = datax.clean_users_data()
# 	experiment.to_csv('experiment_9.csv')


