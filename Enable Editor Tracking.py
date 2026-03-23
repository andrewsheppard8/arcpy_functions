"""
===============================================================================
Script Name:       Enable Editor Tracking
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
Enabling editor tracking on feature class

NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.
===============================================================================
"""

def EditorTracking(geodatabase,feature_class):
    arcpy.env.workspace=geodatabase
    arcpy.management.EnableEditorTracking(feature_class,"Creator","Created",
                                          "Editor","Edited","ADD_FIELDS","UTC")
    arcpy.AddMessage("Editor tracking enabled for feature class")
