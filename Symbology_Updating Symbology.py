"""
===============================================================================
Script Name:       Adding Features to Map & Symbolizing Points/Polygons
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
1. Adding a feature class to a map within an open aprx project
2. Symbolizing point feature class with a unique value render
3. Symbolozing polygon feature class with a black outline.

NOTE: Map object (map_obj) previously created using aprx.CreateMap in parent script.
NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.

===============================================================================
"""

import arcpy
from arcpy import env

#function 1
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

#function 2
def symbolize_studentsfc(map_obj,geodatabase,feature_class):
    aprx_path='CURRENT'
    aprx=arcpy.mp.ArcGISProject(aprx_path)
    arcpy.env.workspace=geodatabase
    arcpy.AddMessage(feature_class)
    aprx = arcpy.mp.ArcGISProject('CURRENT')
    color_ramp_name = "Condition Number"
    color_ramps = aprx.listColorRamps(color_ramp_name)
    if not color_ramps:
        arcpy.AddMessage(f"Color ramp '{color_ramp_name}' not found.")
        return
    color_ramp = color_ramps[0]

    #doing a unique value render based on field value define
    for lyr in map_obj.listLayers():
        if lyr.isFeatureLayer and lyr.name == feature_class:
            sym = lyr.symbology
            if hasattr(sym, 'renderer'):
                sym.updateRenderer('UniqueValueRenderer')
                sym.renderer.fields = ["FIELD"] #FIELD FOR RENDER
                sym.renderer.colorRamp = color_ramp
                lyr.symbology = sym
                arcpy.AddMessage(f"Symbolized {feature_class} based on FIELD field")

#function 3      
def add_district_layer(map_obj, feature_class):
    if arcpy.Exists(feature_class):
        fclass_layer = map_obj.addDataFromPath(feature_class) #adding a feature class to a map
        symbology = fclass_layer.symbology
        symbology.updateRenderer('SimpleRenderer')
        renderer = symbology.renderer
        symbol = renderer.symbol
        symbol.outlineColor = {'RGB': [0, 0, 0]}  # Black outline
        symbol.outlineWidth = 3
        symbol.color = {"RGB": [0, 0, 0, 0]}  # No fill
        district_layer.symbology = symbology
        arcpy.AddMessage('Polygon symbology updated')
    else:
        arcpy.AddMessage("Polygon feature class does not exist")
