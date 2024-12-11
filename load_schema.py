#!/bin/env python3

from sqlalchemy import create_engine, text
from config import Config

# Database engine
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)

# Path to SQL schema
path = 'db/schema.sql'

# Load and execute schema
with engine.connect() as con:
    with open(path, 'r') as file:
        sql_statements = file.read().split(';')
        for statement in sql_statements:
            if statement.strip():  # Skip empty statements
                con.execute(text(statement))
                
print("Schema loaded successfully.")
