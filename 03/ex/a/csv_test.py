import csv
with open('salaries.csv') as f:
  reader = csv.reader(f)
  next(reader) # skip the header
  for row in reader:
    print(float(row[3][1:])) # salaries
