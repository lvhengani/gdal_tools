from osgeo import gdal
import numpy as np
import argparse

def readFile(filename):   
     ds = gdal.Open(filename, gdal.GA_ReadOnly)
     (X, deltaX, rotation, Y, rotation, deltaY) = ds.GetGeoTransform()
     proj = ds.GetProjection()
     geo = ds.GetGeoTransform()
     Nx = ds.RasterXSize
     Ny = ds.RasterYSize
     band = ds.GetRasterBand(1)
     ary = band.ReadAsArray().astype(np.float16)
     nodata = band.GetNoDataValue()
     stats = band.GetStatistics(True, True)
     shape = ary.shape # get the shape of the array
     #ds.Destroy()
     return ary, shape, proj, geo, nodata, stats


if __name__=='__main__':
   filename = 'NDVI_image.TIF'
   ary, shape, proj, geo, nodata, stats = readFile(filename)
   print stats
