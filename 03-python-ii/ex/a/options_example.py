#!/usr/bin/env python

from jamie_census import *

if __name__ == "__main__":

  import argparse
  parser = argparse.ArgumentParser(description='Options example: print ratios from the ACS 2014.  For variables, see: https://api.census.gov/data/2015/acs5/profile/variables.html')
  parser.add_argument('num', type = str, help="numerator field")
  parser.add_argument('den', type = str, help="denominator field")
  parser.add_argument('-l', '--label', type=str, default = "Value", help='Name of Value', metavar = "L")
  parser.add_argument('-r', '--row', type=int, default = -1, help='Number of Lines to Print')
  parser.add_argument('-a', '--abc', action='store_true', default = False, help='print alphabetical instead of head.')
  parser.add_argument('-s', '--state', type=str.lower, default = "", help = "county estimates for state s; otherwise US by state", metavar = "st", choices = [""] + list(state_fips.keys()))

  args = parser.parse_args()
  print(args)

  # census_table(state = args.state, name = args.label, num = args.num, den = args.den, head = args.row, sort_abc = args.abc)

