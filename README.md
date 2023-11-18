# the_MRDC_project
A repo for the Multinational Retail Data Centralisation project

# The Multinational Retail Data Centralisation
A data wharehouse is built in a local postgres database (target db), for collecting and organising specific data retrieved from various sources 
The data is pulled from S3 AWS (Amazon Web Services) in various formats,cleaned and copied to db *sales_data*, in which the final six tables are organised in a star-based schema (see which primary and foreign keys are in my_schema.pdf)

## Table of Contents
The suite of programs that generates and populates the target database are named as follows:
    main.py
    data_extraction.py
    data_cleaning.py
    data_utils.py

The databases' credential files, added to .gitignore and required for creating the connection engine, are as follows:
    target_creds.yaml
    source_creds.yaml

The directory, queries/, contains both queries in .mssql files for reproducing the outputs, and the snapshot of the outputs when tested as fiiles .png

### Description of the project:
 The project was developed in four stages, as follows:
   
   - Set a local database (db) called sales_data (use postgres pgadmin4), in which to store and query the six tables
   
   - Create four object-oriented python scripts for extracting, transforming and loading data (e.g the ETL pipelines)
       - data_extraction.py with class DataExtractor()
       - database_utils.py with class DatabaseConnector()
       - data_cleaning.py with class DataCleaning()
       - main.py with six pipelines, one per table
   
   - Create a database schema (how the tables are linked in the database)
       - primary key in five tables; foreign keys to orders table
       - star-based schema, see my_schema.pdf
       
   - Query data (SQL code scripts: .mssql files, and pgadmin4 outputs as .png): queries 1,2,4 8 are complete; and queries 3,5,6,7,9 work-in-progress
   
### Updates
Nov 16,2023: the six pipelines are functional and complete. Nov 18,2023: the complete queries included, a new README file is uploaded.

### Usage Instructions
For testing and/or further development of this program suite, do select specific pipelines by uncommenting the relevant lines in the main.py; to launch the suite to populate the local database, uncomment all six pipelines in main.py and do as follows (either way):

 	    % python3 main.py   
        % python3 main.py > output.log   

### Licence Information
This program suite is not covered by licence. It was built in partial fullfilment of the requirements for the AICore Data Engineering certification. I want to acknowledge the AiCore Team for their invaluable support: Thanks!