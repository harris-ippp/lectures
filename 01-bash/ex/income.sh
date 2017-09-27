#!/bin/bash

# Download the data from the census
# DP05_0001E  :: Total population
# DP03_0062E  :: Median Income
# DP03_0119PE :: Poverty Rate
curl "https://api.census.gov/data/2014/acs5/profile?for=county:*&in=state:*&get=NAME,DP05_0001E,DP03_0062E,DP03_0119PE" -o income.json

# poorest counties.
echo "Poorest Counties"
tail -n +2 income.json |     # print all but the first line.
     sed 's/[][]//g' |       # get rid of the brackets
     sed "s/\",\"/:/g" |     # replace field delimiters with colons
     sed "s/\"//g" |         # remove quotes
     sed "s/,$//" |          # drop commas at end of lines
     grep -v "Puerto Rico" | # exclude PR 
     sort -t: -n -r -k 4 |   # sort the columns
     head -10 |              # top 10
     column -t -s":"         # clean it up

echo

# Same thing for the richest counties -- just another column.
echo "Richest counties"
tail -n +2 income.json | sed 's/[][]//g' | sed "s/\",\"/:/g" | sed "s/\"//g" | sed "s/,$//" | grep -v "Puerto Rico" |
    sort -t: -n -r -k 3 | head -10 | column -t -s":" 

