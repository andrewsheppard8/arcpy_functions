"""
===============================================================================
Script Name:       Enable Editor Tracking
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             asheppard@mgt.us
Date Created:      2026-03-23

Description:
-------------
Enabling editor tracking on feature class

Part of a larger script. To see original usage, see Geocoding from Excel script in arcpy_scripts

Follow link for full description of ESRI tool:
https://pro.arcgis.com/en/pro-app/3.4/tool-reference/data-management/enable-editor-tracking.htm

===============================================================================
"""

def EditorTracking(geodatabse,feature_class):
    arcpy.env.workspace=geodatabase
    arcpy.management.EnableEditorTracking(feature_class,"Creator","Created",
                                          "Editor","Edited","ADD_FIELDS","UTC")
    arcpy.AddMessage("Editor tracking enabled for feature class")
