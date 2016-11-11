#/usr/bin/python

from osgeo import ogr
import argparse

description="A script for detrmining fields in a shapefile"
parser=argparse.ArgumentParser(description=description)
parser.add_argument('shapefile',help='A full path to a shapefile of interests')

args = parser.parse_args()

shapefile=args.shapefile

datasource = ogr.Open(shapefile)
datalayer = datasource.GetLayer(0)
layerDefinition = datalayer.GetLayerDefn()

field_counts = layerDefinition.GetFieldCount()
fields = []

for cnt in range(field_counts):
   fields.append(layerDefinition.GetFieldDefn(cnt).GetName())

if field_counts>1:
   print "The layer has {} fields".format(field_counts)
else:
   print "The layer has {} field".format(field_counts)

print fields
