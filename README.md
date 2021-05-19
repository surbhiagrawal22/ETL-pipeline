# ETL-pipeline
                        ** ETL pipeline in Python **

                        ** About the dataset **

•	The dataset includes a record for each oil pipeline leak or spill reported to the Pipeline and Hazardous Materials Safety Administration since 2010 till 2016. These records include the incident date and time, operator and pipeline, cause of incident, type of hazardous liquid and quantity lost, injuries and fatalities, and associated costs. Dataset has been taken from kaggle and was saved in Postgre database.

                         ** Setup of files **

•	A credentials.py file is used which stores all the database connection user ID/password, environmental variables for security purpose.

•	SQL_query.py file is used which stores the code for connecting to MYSQL database.

•	AccidentsModel.py where the business ML question and OLAP based query is solved.

•	Tried Logging of each step used in ETL pipeline in ETLlogfile.log for debugging purpose. Same can be used for ETL testing.

•	After deletion of any rows and columns, the dropped rows/columns have been saved in a .csv file. Can be used for testing purpose also.
The three files generated and saved are Duplicated_rows.csv, Duplicated_columns.csv, Constant_value_column.csv.

•	Profiling of input dataset has been done using the Pandas profiling library and the .html file is used as Oil_Pipeline_Accident.html. It informs about missing values, cardinality, inconsistency in the data. This file further helped in transforming the dataset.

All the above .py (credentials.py. and SQL_query.py) modules needs to be saved in same folder while running the main file which is ETLExtractTransformLoad.py file.

                              ** ETL Pipeline **

•	ETLExtractTransformLoad.py contains the code for extracting data from Postgre SQL database. Connection is made to the Postgre Database and dataset is read.

•	The extracted data is then cleaned and scrubbed using procedural programming (step by step calling of each function and output of a function becomes input for another function). 

•	Data is cleaned on basis of Consistency, Uniqueness dimension. Duplicate rows, duplicate columns and constant value columns have bene removed.

•	Inconsistent values have been replaced and white spaces has been trimmed.

•	The star schema (1 fact table and 7 dimension tables) has been created and all the files are staged in a local database MYSQL Datawarehouse.


                         ** Solving business Use-case **

•	In AccidentsModel.py, the data in form of star schema is first read from the MYSQL database by creating connection and running SQL queries.

•	OLAP question and Machine learning model has been solved in AccidentsModel.py.

•	Decision tree classifier and Random Forest Classifier both has been applied to predict the liquid type which has caused the Oil Spill
Altough the accuracy with both models is low, but with random forest classifier , accuracy has increased significantly by 10 % .
