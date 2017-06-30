"""
Download GeoJSON data for Cincinnati's neighbourhoods.
Not currently working; meant to replicate the behaviour of:
esri2geojson https://services.arcgis.com/JyZag7oO4NteHGiq/arcgis/rest/services/CPD_Neighborhoods/FeatureServer/0 maps/CPD_Neighborhoods.json
"""

import json
from esridump.dumper import EsriDumper

DATA = EsriDumper('https://services.arcgis.com/JyZag7oO4NteHGiq/arcgis/rest/services/CPD_Neighborhoods/FeatureServer/0')

print(json.dumps(DATA))
