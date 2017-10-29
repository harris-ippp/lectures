import pandas as pd

pd.read_html("https://harris-ippp.github.io/lectures/")

wiki =  "https://en.wikipedia.org/wiki/"
wiki += "List_of_colleges_and_universities_"
wiki += "in_the_United_States_by_endowment"
pd.read_html(wiki)
