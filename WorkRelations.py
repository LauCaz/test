from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from qgis.gui import *
import processing
from datetime import datetime

origins = QgsVectorLayer("/Users/laca/Documents/QGIS Work/A3.shp","origins","ogr")
destinations = QgsVectorLayer("/Users/laca/Documents/QGIS Work/A5.shp","destinations","ogr")

L = origins.fields().names()
print(L)

for i in range (2,17):
    id_list = []
    print(datetime.now())
    field = L[i]
    for f in origins.getFeatures():
        if f[field]>0:
            id_list.append(f.id())
    print(id_list)
    origins.selectByIds([k.id() for k in id_list])
    destinations.selectByIds([k.id() for k in id_list])
    
    processing.run("saga:pointdistances", {'POINTS':QgsProcessingFeatureSourceDefinition('C:/Users/laca/Documents/QGIS Work/A3.shp', selectedFeaturesOnly=True, featureLimit=-1, geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),'ID_POINTS':'Ruta','NEAR':QgsProcessingFeatureSourceDefinition('C:/Users/laca/Documents/QGIS Work/A5.shp', selectedFeaturesOnly=True, featureLimit=-1, geometryCheck=QgsFeatureRequest.GeometryAbortOnInvalid),'ID_NEAR':'Ruta','FORMAT':1,'MAX_DIST':20000,'DISTANCES':str(i)+'.dbf'})   
   
