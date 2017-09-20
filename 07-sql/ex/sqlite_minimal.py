import sqlite3

con = sqlite3.connect("atus.sqlite")
result = con.execute("SELECT case_id, line_no, family_income "
                      "FROM cps WHERE line_no = 1 " 
                      "LIMIT 10")

for row in result: print(row)
