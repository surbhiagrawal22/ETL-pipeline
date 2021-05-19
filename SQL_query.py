import credentials as creds
from mysql.connector import connect,Error

### https://stackoverflow.com/questions/50557234/authentication-plugin-caching-sha2-password-is-not-supported
"""In MySQL 8.0, caching_sha2_password is the default authentication plugin rather than mysql_native_password."""

host=creds.host
user=creds.user
password=creds.password


def create_conenction(host,user,password):
   try: 
    connection=connect(host=host,user=user,password=password,auth_plugin='mysql_native_password')
    print(f'connection is successful {connection}')
   except Error as e:
       print(e)
   finally:
     return connection

    
def create_cursor(connection):
    cursor=connection.cursor()
    return cursor


def execute_query(cursor,query,connection):
    
    cursor.execute(query)
    connection.commit()

    
    
drop_database="""DROP DATABASE IF EXISTS accident"""
create_database ="CREATE DATABASE accident"
use_database="""USE accident"""



def create_db(cursor,connection):
   
    execute_query(cursor,drop_database,connection)
    execute_query(cursor,create_database,connection)
    execute_query(cursor,use_database,connection)

    print("Succesfully connected to Data Warehouse MYSQL")
