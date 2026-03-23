"""
===============================================================================
Script Name:       Updating Symbology for feature classes
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             asheppard@mgt.us
Date Created:      2026-03-23

Description:
-------------
This is a simple script showing a common process of how to add fields to a
feature class in a geodatabase. This process will loop through all fields in the feature
class, and if the field exists, it will skip it. If it does not exist, it will create it.
This isn't a full breakdown of the syntax of the Arcpy Add Field tool.

This function can be copied directly to create a simple Geoprocessing tool in a custom toolbox
within ArcGIS Pro.

Follow link for full description of ESRI tool:

https://pro.arcgis.com/en/pro-app/3.4/tool-reference/data-management/add-field.htm

===============================================================================
"""

def add_feature_class_layers(map_obj,students_path,student_fc):
    aprx_path='CURRENT'
    aprx=arcpy.mp.ArcGISProject(aprx_path)
    arcpy.env.workspace=students_path
    studfc_name=student_fc
    stud_fc=os.path.join(students_path, studfc_name)
    if arcpy.Exists(stud_fc):
            lyr = map_obj.addDataFromPath(stud_fc)
            arcpy.AddMessage(f"Added {student_fc} to the map")
            lyr.visible = True
                
    else:
        arcpy.AddMessage(f"{student_fc} does not exist")
def symbolize_studentsfc(map_obj,students_path,student_fc):
    aprx_path='CURRENT'
    aprx=arcpy.mp.ArcGISProject(aprx_path)
    arcpy.env.workspace=students_path
    arcpy.AddMessage(student_fc)
    aprx = arcpy.mp.ArcGISProject('CURRENT')
    color_ramp_name = "Condition Number"
    color_ramps = aprx.listColorRamps(color_ramp_name)
    
    if not color_ramps:
        arcpy.AddMessage(f"Color ramp '{color_ramp_name}' not found.")
        return
    color_ramp = color_ramps[0]
    
    for lyr in map_obj.listLayers():
        if lyr.isFeatureLayer and lyr.name == student_fc:
            sym = lyr.symbology
            if hasattr(sym, 'renderer'):
                sym.updateRenderer('UniqueValueRenderer')
                sym.renderer.fields = ["RESIDENT"]
                sym.renderer.colorRamp = color_ramp
                #sym.renderer.addAllValues()
                lyr.symbology = sym
                arcpy.AddMessage(f"Symbolized {student_fc} based on RESIDENT field")
def add_district_layer(map_obj, district):
    if arcpy.Exists(district):
        district_layer = map_obj.addDataFromPath(district)
        symbology = district_layer.symbology
        symbology.updateRenderer('SimpleRenderer')
        renderer = symbology.renderer
        symbol = renderer.symbol
        symbol.outlineColor = {'RGB': [0, 0, 0]}  # Black outline
        symbol.outlineWidth = 3
        symbol.color = {"RGB": [0, 0, 0, 0]}  # No fill
        district_layer.symbology = symbology
        arcpy.AddMessage('District symbology updated')
    else:
        arcpy.AddMessage("District feature class does not exist")
