#Z point to 3d 

import geopandas as gpd
import matplotlib
from shapely import Polygon, LineString, Point

layer_selected=iface.layerTreeView().selectedLayers()[0]

coordinate=[] #[(x0,y0,z0),(x1,y1,z1),...]
crs="EPSG:3857"

for feature in layer_selected.getFeatures():
    print(feature['Z']) #Z column, this column must be set in the attribute with the name "Z"
    print(feature.geometry().asPoint().x()) #X coordinate
    print(feature.geometry().asPoint().y()) #Y coordinate
    coordinate+=[(feature.geometry().asPoint().x(),feature.geometry().asPoint().y(),feature['Z'])]
  
print(coordinate)

data=[{'name':'test'}]
geom=gpd.GeoSeries(Polygon(coordinate))

df=gpd.GeoDataFrame(data,geometry=geom,crs=crs)

df.to_file('df.geojson', driver='GeoJSON')
