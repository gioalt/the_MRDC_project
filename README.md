# the_MRDC_project
A repo for the Multinational Retail Data Centralisation

# The Multinational Retail Data Centralisation
A data wharehouse is built in a local postgres database (target db), for collecting and organising specific data retrieved from various sources 
The data is pulled from S3 AWS (Amazon Web Services) in various formats,cleaned and copied to *sales_data* db,where the final tables are organised in a star-based schema (see my_schema.txt/pdf)

## Table of Contents
The files that generate/populate the target database are as follows:
    main.py
    data_extraction.py
    data_cleaning.py
    data_utils.py

The db credential files, added to .gitignore and required for connecting to databases, are as follows:
    target_creds.yaml
    source_creds.yaml


### Description of the project:
 There are four milestones to accomplish within November the 16, 2023. These are as follows:
   
   - Set a database (db) called *sales_data* (use pgadmin4): will contain info extracted from data resources
   
   - Create 3 python scripts, one per classes, for extracting, connecting and cleaning data (*ten tasks*)
       - *data_extraction.py* with class DataExtractor()
       - *database_utils.py* with class DatabaseConnector()
       - *data_cleaning.py* with class DataCleaning()
       - *main.py* with six pipelines, one per table

   
   - Create a database schema (how the db connects tables)
       - primary key in dimensions tables; foreign keys to orders table
       - star-based schema, see my_schema.txt.pdf
       
   - Query data (SQL code scripts, .mssql files)
   
### UPDATES
Nov 14, 2023: the six pipelines are functional and almost complete, with the exception of cleaning of a couple of tables.
the prefix my_ signifies I plan to perform further development. the queries are not yet finalised at the moment (only tests have been performed)

### INSTRUCTIONS
for testing or development of these programmes suite select each specific pipeline by uncommenting them in main.py; then, launch
pipelines to populate the local database as follows:
 
 	% python3 main.py
or 
	% python3 main.py > output.log