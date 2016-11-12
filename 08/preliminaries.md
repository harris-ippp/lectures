# Installation of Geographical Libraries

Geographical libraries are reliably the toughest packages to install, since they rely on c++ code that does not always compile well.  In order to open 'shapefiles,' which map files, we need a library called Fiona.  Conda is able to install fiona pretty much out of the box on Macs, but on PCs... not so much.  We have been using python 3.5, which I could not get to run.  Fortunately, conda makes it really easy to use different versions of python as 'environments.'  By setting up an environment `p34-geo`, we can just run 

## Mac

Lucky kids -- this is it -- 
* `conda install fiona`
* `conda install -c conda-forge geopandas`
* `conda install -c conda-forge folium`
* `conda install -c conda-forge mplleaflet`
* `conda install jupyter wget pysal`

## PC

Set up the virtual environment and install the packages
* `conda create -n p34-geo python=3.4`
* `source activate p34-geo`
* `conda install fiona "libgdal<2.0"`
* `conda install pandas matplotlib`
* `conda install -c ioos shapely pyproj`
* `conda install -c ioos geopandas descartes --no-deps`
* `conda install -c conda-forge folium`
* `conda install -c conda-forge mplleaflet`
* `conda install jupyter wget pysal`

(Adapted from [here](https://www.bountysource.com/issues/27623893-fyi-installing-geopandas-with-conda).)
