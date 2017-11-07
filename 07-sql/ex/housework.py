import sqlite3, pandas as pd

con = sqlite3.connect("atus.sqlite")

with open("ex/housework.sql") as f:
    df = pd.read_sql(f.read(), con)
      
ax = df[df.sex == 2].plot(x = "ed", y = "housework",
                          label = "Women")
df[df.sex == 1].plot(x = "ed", y = "housework", 
                     label = "Men", ax = ax)

ax.set_ylabel("Average Daily Housework [Hours]")
ax.set_xlabel("Education [Years]")

ax.figure.savefig("housework.pdf")
