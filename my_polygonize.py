#!/usr/bin/python
import os
import argparse

"""
By L M Vhengani
Date: 2016-06-23 
Purpose: This utility can be used to polygonize geotiff files to shapefiles. 
         It is an enhancement of the uility gdal_polygonize.py. 
Requirements: GDAL/OGR must be installed in order to use this utility. 
Usage: python my_polygonize [in_rasterfile] [out_shapefile] [--where filter_function]
"""


# A function for polygonizing a raster and output polygons whose DN is not zero and in WGS84 spatial regerence system
def polygonize(in_rasterfile,out_shapefile,where='DN!=0',out_src='EPSG:4326'):
    #polygonize
    out_shapefile_temp = out_shapefile[:-4]+'_temp1.shp'
    os.system('gdal_polygonize.py {} -q -f "ESRI Shapefile" {}'.format(in_rasterfile,out_shapefile_temp))
    #remove polygons with zeros and project results to wgs84
    select_string = 'ogr2ogr -where "{0}" -t_srs {1} {2} {3}'.format(where,out_src,out_shapefile,out_shapefile_temp)
    os.system(select_string)
    # Delete temporary files
    os.system('rm {}*'.format(out_shapefile_temp[:-3]))
    print "Polygonized {} to {} done!".format(os.path.basename(in_rasterfile),os.path.basename(out_shapefile))


parser = argparse.ArgumentParser(description='Process an image to polygons.')
parser.add_argument('in_rasterfile', help='an input raster file')
parser.add_argument('out_shapefile', help='an output shapefile')
parser.add_argument('--where', type=str, default=None, help='A function to use for filtering polygons with unwanted DN values. The default is "DN!=0"')

args = parser.parse_args()
in_rasterfile = args.in_rasterfile
out_shapefile = args.out_shapefile
where = args.where

if where:
   polygonize(in_rasterfile,out_shapefile,where)
else:
   polygonize(in_rasterfile,out_shapefile)
