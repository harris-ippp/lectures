import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

st_map = gpd.read_file("data/state_map.shp").set_index("state")

def plot_states(s):

    s = pd.Series(s, name = "S")
    ax = st_map.join(s).plot(column = "S", scheme = "quantiles", k = 10, 
                             cmap = "viridis", alpha = 0.8, figsize = (5, 5),
                             linewidth = 1, edgecolor = "black", legend = True)

    ax.set_axis_off()
    ax.get_legend().set_bbox_to_anchor((1.40, 1))
    
    plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, hspace = 0, wspace = 0)
    plt.margins(0,0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())


