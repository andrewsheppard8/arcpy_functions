"""
===============================================================================
Script Name:       Running Secondary Script within a Geoprocessing Tool
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
This important function will call a tool within a specified toolbox as part of a
script.
===============================================================================
"""
studyareas=arcpy.GetParameterAsText(0)
destination=arcpy.GetParameterAsText(1)
toolbox_path = r"PATH_TO_TOOLBOX"
if arcpy.Exists(toolbox_path):
    arcpy.AddMessage("toolbox exists")
    arcpy.ImportToolbox(toolbox_path,"custom_tools")
    arcpy.AddMessage("Toolbox imported")
    try:
        arcpy.custom_tools.TOOLNAME(studyareas,destination)
        arcpy.AddMessage("Tracts Update second tool executed successfully")
    except Exception as e:
        arcpy.AddMessage(f"Error running Dissolve Tool: {e}")
