from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from config import Config
import os

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

sql_file_path = 'db/schema.sql'

# Function to execute SQL commands from a file
def execute_sql_file(engine, sql_file_path):
    with open(sql_file_path, 'r') as file:
        sql_commands = file.read()
    
    with engine.connect() as connection:
        with connection.begin() as transaction:
            for command in sql_commands.split(';'):
                command = command.strip()
                if command.startswith('--') or  command.startswith('/*') or not command:
                    continue
                connection.execute(text(command))

execute_sql_file(engine, sql_file_path)

print("SQL file loaded successfully.")