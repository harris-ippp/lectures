import sqlite3, pandas as pd

con = sqlite3.connect("atus.sqlite")
cps = pd.read_sql_query("""
           SELECT case_id, line_no, family_income 
           FROM cps WHERE line_no = 1 
           LIMIT 10""", 
           con, index_col = "case_id")

print(cps)
