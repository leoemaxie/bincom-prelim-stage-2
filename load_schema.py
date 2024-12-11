#!/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

path = 'db/schema.sql'

# Execute SQL commands from a file
with engine.connect() as con:
    with open(path) as file:
        query = text(file.read())
        con.execute(query)

print("Schema loaded successfully.")