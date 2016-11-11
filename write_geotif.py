from osgeo import gdal

# Write the data to geotif
def WriteGeoTif(array,outname,shape1,proj1,geo1,directory=None):       
    driver = gdal.GetDriverByName('GTiff')
    ds = driver.Create(outname,shape1[1],shape1[0],1,gdal.GDT_Float32,options=['COMPRESS=DEFLATE'])
    ds.SetGeoTransform(geo1)
    ds.SetProjection(proj1)
    ds.GetRasterBand(1).WriteArray(array)
    #stat = ds.GetRasterBand(1).GetStatistics(1,1)
    #ds.GetRasterBand(1).SetStatistics(stat[0],stat[1],stat[2],stat[3])
