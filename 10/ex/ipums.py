import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

headers = ["YEAR", "DATANUM", "SERIAL", "HHWT", "REGION", "STATEICP", "STATEFIP", "COUNTY",
           "SIZEPL", "PUMA", "GQ", "PERNUM", "PERWT", "SEX", "AGE", "MARST", "BIRTHYR",
           "MARRNO", "BPL", "BPLD", "EDUC", "EDUCD"]

def weighted_average(grp):
  return grp._get_numeric_data().multiply(grp['PERWT'], axis=0).sum()/grp['PERWT'].sum()


def make_map(yr, val, title):

  df = pd.read_csv('data/{}.csv'.format(yr), names=headers,
                   usecols = ["AGE", "BPL", "EDUCD", "PERWT", "STATEFIP"])

  df['COLLEGE_GRAD'] = df['EDUCD'] > 100
  df['HS_GRAD']      = df['EDUCD'] > 62

  req = (df['BPL'] < 57) & (30 < df['AGE']) & (df['AGE'] < 50)
  req &= (df['BPL'] != 2) & (df['BPL'] != 15)
  us_adults_df = df[req]

  grads = us_adults_df.groupby("BPL").apply(weighted_average)

  state_frame = gpd.read_file("cb_state/cb_2015_us_state_20m.shp")
  state_frame["STATEFP"] = pd.to_numeric(state_frame["STATEFP"])

  state_grads = state_frame.merge(grads, how = "inner", left_on = "STATEFP", right_on='BPL')

  kwargs = dict(figsize = (15, 10), linewidth = 0.5, legend = True,
                scheme='QUANTILES', k=5, alpha = 0.8, cmap='PuOr')

  ax = state_grads.to_crs(epsg = 2163).plot(column = val, **kwargs)
  ax.set_title("{}, Born {} - {} (by Quintile)".format(title, yr-50, yr-30), fontsize = 20)
  ax.set_axis_off()

  plt.savefig("{}.png".format(yr), dpi = 200, bbox_inches='tight')