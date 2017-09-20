#!/bin/bash

# SORT CHICAGO SALARIES

# start the party!!
echo "Top 10 Salaries in Chicago"
cat salaries.csv | \
    # get keep only lines with dollar signs.
    grep '\$' | \

    # remove the dollar signs and quotes
    sed 's/\$//g' | sed "s/\"//g" | \

    # sorting is the best.
    sort -t, -k 5 -n -r | \

    # clean it up
    head -10 | column -s, -t


# How many police officers are there?
echo "Police Officers in Chicago"
cat salaries.csv | \

    # look for police officers
    grep "POLICE OFFICER" | \

    # count 'em with wc!
    wc -l


# How many police detectives are there?
echo "Police Officers in Chicago"
cat salaries.csv | \

    # look for police officers assigned as detectives
    grep "POLICE OFFICER.*DETECTIVE" | \

    # count 'em with wc!
    wc -l


# What are the most common names of police officers?
cat salaries.csv | 

    # grab police officers.
    grep "POLICE OFFICER" | \
    
    # grab their names
    cut -d "," -f 2 | \
    
    # get rid of quotes and leading spaces
    sed "s/\"//g" | sed "s/^ *//g" | \
      
    # choose the first field.
    cut -d " " -f 1 | \
    
    # do some sorting magic to pull off the top 40
    sort | uniq -c | sort -r | head -40

# What do you notice about the names?  Ouff.
