import wget
import os

import geopandas as gpd
from shapely.geometry import Point

# wget.download("http://www2.census.gov/geo/tiger/GENZ2014/shp/cb_2014_17_tract_500k.zip")
# os.system("unzip cb_2014_17_tract_500k.zip")
tract_df = gpd.read_file("cb_2014_17_tract_500k.shp")
tract_df = tract_df[tract_df['COUNTYFP'] == '031'][["geometry", "NAME"]]

crime_df = pd.read_csv("data/Crimes_-_2001_to_present.csv", usecols = [19, 20])
crime_df.dropna(inplace = True)

geometry = [Point(xy) for xy in zip(crime_df.Longitude, crime_df.Latitude)]
crime_coords = gpd.GeoDataFrame(crime_df, crs = tract_df.crs, geometry=geometry)

located_crimes = gpd.tools.sjoin(crime_coords, tract_df, how = 'left', op = 'within')

located_crimes.rename(columns = {"NAME" : "Census Tract", "index_right" : "Total Crimes"}, inplace = True)

crime_tract_count = located_crimes.groupby("Census Tract").count()[["Total Crimes"]]

crime_tract_count.sort_values(by = "Total Crimes", ascending = False)
crime_tract_count.to_csv("data/crime_tract_count.csv")

