#!/bin/bash

grep '\$' salaries.csv | sed 's/\$//g' | sed "s/\"//g" | sort -t, -k 5 -n -r | head -30 | column -s, -t
