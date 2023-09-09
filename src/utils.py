# Importing necessary modules

import os
 
from typing import *
import mysql.connector
from mysql.connector import Error

# Loading environment variables
def load_envs() -> Dict:
    
    try:
        
        env_vars = {}
        env_vars['ENVIRONMENT'] = os.getenv('ENVIRONMENT')
        env_vars['DB_HOST'] = os.getenv('DB_HOST')
        env_vars['DB_PORT'] = os.getenv('DB_PORT')
        env_vars['DB_USER'] = os.getenv('DB_USER')
        env_vars['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
        
        if env_vars['ENVIRONMENT'] == 'prd':
            env_vars['AWS_KEY_IAM'] = os.getenv('AWS_KEY_IAM')
            env_vars['AWS_SECRET_IAM'] = os.getenv('AWS_SECRET_IAM')
            
        print('All environment variables:')
        print([values for values in env_vars.values()])
        
        return env_vars
    
    except Exception as e:
        print(f'Error occured while loading environment varibales: {e}')
        return None
    
    
def load_mysql(env_vars : Dict) -> None:
    
    try:
        
        global connection
        global cursor
        
        connection = mysql.connector.connect(
            host = env_vars['DB_HOST'],
            port = env_vars['DB_PORT'],
            user = env_vars['DB_USER'],
            password = env_vars['DB_PASSWORD']
        )
        
        if connection.is_connected():
            cursor = connection.cursor(buffered = True)
            cursor.execute('SHOW DATABASES;')
            databases = cursor.fetchall()
            if 'db_emp' in [db[0] for db in databases]:
                print(f'\nDatabase \'db_emp\' is available in MySQL Server on host {env_vars["DB_HOST"]} in Environment {env_vars["ENVIRONMENT"]}')
                print('All Databases:')
                print([db[0] for db in databases])
            
            else:
                print('Connection somehow not possible')
                
            cursor.close()
            connection.close()
            
        else:
            print('Connection not enabled')
        
    except Error as e:
        print(f'Error occured while connecting to MySQL DATABASE on host {env_vars["DB_HOST"]} in Environment {env_vars["ENVIRONMENT"]}')
        print(f'Error: {e}')
        
def hello_world():
    print('Hello World')