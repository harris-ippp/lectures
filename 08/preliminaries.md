# Installation of Geographical Libraries

Geographical libraries are reliably the toughest packages to install, since they rely on c++ code that does not always compile well.  In order to open 'shapefiles,' which map files, we need a library called Fiona.  Conda is able to install fiona pretty much out of the box on Macs, but on PCs... it is [quietly unsupported](https://docs.continuum.io/anaconda/pkg-docs).  We have been using python 3.5, for which even the underlying libraries (gdal) didn't work.  Fortunately, conda makes it really easy to use different versions of python as 'environments.'  By setting up an environment `p34-geo`, we can install without too much trouble.

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
  * If this fails, complaining about \r, etc., then Windows is refusing to understand the end of line characters, and you need to get rid of them.  You can do this using `sed`:
  
    ```
    sed -i "s/\r$//" /the/path/it/complained/about/Scripts/activate
    sed -i "s/\r$//" /the/path/it/complained/about/Scripts/deactivate
    ```
    (Copy the path from what you see failing, but be weary to "escape" any spaces: `../James\ Saxon/Anacond3/...`)
    
* `conda install fiona "libgdal<2.0"`
* `conda install pandas matplotlib`
* `conda install -c ioos shapely pyproj`
* `conda install -c ioos geopandas descartes --no-deps`
* `conda install -c conda-forge folium`
* `conda install -c conda-forge mplleaflet`
* `conda install jupyter wget pysal`

Pour yourself a glass of wine.

(Adapted from [here](https://www.bountysource.com/issues/27623893-fyi-installing-geopandas-with-conda).)
