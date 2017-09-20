#!/bin/bash

# We have several questions about 
# the time distribution of first 
# degree murders.  Let's make an
# 'intermediate' file with just 
# that information.
cat chicago_crime.csv | \
    
    # grep out the first degree murders
    grep "FIRST DEGREE MURDER" | \

    # use cut to select the date (3rd field, divided by ",")
    cut -d "," -f3 | \

    # write it
    cat > murder_dates.txt 


echo "Murders by hour of day."
cat murder_dates.txt | \

    # use sed to find minutes and seconds, and remove them.
    sed "s/:..:.. //" | \

    # choose out only the times -- the 2nd field, delimited by spaces.
    cut -d " " -f2 | \

    # we'll sort it, so we want 12AM to come before 01AM
    # use sed to replace 12 with 00
    sed "s/12/00/" | \

    # sort it and count the results
    # (try not sorting too -- what goes wrong.)
    sort | uniq -c | \

    # sort and grab the worst hour
    sort | tail -1


echo "Worst month for murders."
cat murder_dates.txt | \

    # slice "/" to grab the month (1st field)
    cut -d "/" -f 1 | \
      
    # sort them, then count.
    sort | uniq -c | head -1 


echo "Bloodiest single day."
cat murder_dates.txt | \

    # we just want the dates, no times
    cut -d " " -f1 | \

    # sort and count
    sort | uniq -c | \

    # reverse sort and take the top one
    # (or, of course, sort and take the last)
    sort -r | head -1


echo "Murders by place."
cat chicago_crime.csv | \
      
    # Use grep to grab the first degree murders
    grep "FIRST DEGREE MURDER" | \
      
    # use cut to select the place field.
    cut -d "," -f 8 | \
      
    # sort it so that you can count (uniq).
    sort | uniq -c | \
      
    # then (reverse) sort  _that_, to order by the common places.
    sort -r | head -1



