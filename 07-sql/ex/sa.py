#!/usr/bin/env python 

import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('sqlite:///atus.sqlite')

import sqlite3

query = ""
for l in open("ex/family.sql"): query += l
print(query)

con = sqlite3.connect("atus.sqlite")
df = pd.read_sql_query(query, con)

print(df)


