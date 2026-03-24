"""
===============================================================================
Script Name:       Adding Features to Map & Symbolizing Points/Polygons
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
Adding a feature class to a map within an open aprx project

NOTE: Map object (map_obj) previously created using aprx.CreateMap in parent script.
NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.
===============================================================================
"""

import arcpy
from arcpy import env

def add_feature_class_layers(map_obj,geodatabase,feature_class):
    aprx_path='CURRENT'
    aprx=arcpy.mp.ArcGISProject(aprx_path)
    arcpy.env.workspace=geodatabase
    fc_name=feature_class
    fc_full=os.path.join(geodatabase, feature_class)
    if arcpy.Exists(fc_full):
            lyr = map_obj.addDataFromPath(fc_full) #adding a feature class to a map
            arcpy.AddMessage(f"Added {fc_full} to the map")
            lyr.visible = True #turns on visibility for layer       
    else:
        arcpy.AddMessage(f"{fc_full} does not exist")
