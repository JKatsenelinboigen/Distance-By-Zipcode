import sys
import pandas as pd
import os
import pathlib
cwd = pathlib.Path(__file__).parent.absolute() #current working directory for relative path to dataset
from geopy.distance import geodesic


class ZipCodeDatasetParser:
    datasetFile = None
    opendataset = None
    def loadZipCSV(self):
        
        #reference opendataset by current directory/dataset
        self.datasetFile = str(cwd) + "\\dataset\\us-zip-code-latitude-and-longitude.csv" 
        try:

            ##read csv and ensure zip codes are treated as strings to avoid leading zero problem
            self.opendataset = pd.read_csv(self.datasetFile)
            self.opendataset['Zip'] = self.opendataset['Zip'].astype(str).str.zfill(5) 
        except:
            print("Invalid Dataset, check your datasets directory")


    #returns tuple of form (lat, long)
    def getZipCoordinates(self, strZip):
        od = self.opendataset
        if(od is None):
            print("Invalid Dataset, check your init function")
            return ()
        
        #Searches for lattitude and longitude of each zip the zip code
        #zip codes treated as strings avoid leading 0 problem
        lattitude = od.loc[od['Zip'] == strZip]["Latitude"] 
        longitude = od.loc[od['Zip'] == strZip]["Longitude"]
        try:
            coords = (float(lattitude), float(longitude))
        except:
            print("Zip code: " + strZip + " was not found in the dataset.")
            return (None, None)
        return (coords)

    

    def distanceBetweenCoordsMi(self, coord1, coord2):
        return(geodesic(coord1, coord2).miles)

    def distanceBetweenCoordsKm(self, coord1, coord2):
        return(geodesic(coord1, coord2).kilometers)

    def distanceBetweenZipsMi(self, zip1, zip2):
        z1 = self.getZipCoordinates(zip1)
        z2 = self.getZipCoordinates(zip2)

        #if the zip code is not found, null is returned 
        if(None in z1 or None in z2):
            return None
        return self.distanceBetweenCoordsMi(z1, z2)

    def distanceBetweenZipsKm(self, zip1, zip2):
        z1 = self.getZipCoordinates(zip1)
        z2 = self.getZipCoordinates(zip2)

        #if the zip code is not found, null is returned 
        if(None in z1 or None in z2):
            return None
        return self.distanceBetweenCoordsKm(z1, z2)
    
    def __init__(self,):
        self.loadZipCSV()
    