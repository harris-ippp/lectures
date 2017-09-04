#!/bin/bash
#^^ which language?

# SORTING CHICAGO SALARIES <<< A comment
# Comments make your TAs happy and get you points.

echo "Top 10 Salaries in Chicago::"
cat salaries.csv |        # start the party!!
    grep '\$' |           # keep lines with dollar signs
    sed 's/\$//g' |       # remove the dollar signs ...
    sed "s/, //g" |       # and commas in names
    sort -t, -k 7 -n -r | # sorting is the best.
    head -10 |            # top ten
    column -s, -t         # clean it up
