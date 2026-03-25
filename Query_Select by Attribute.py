"""
===============================================================================
Script Name:       Select by Attribute Query
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-25

Description:
-------------
This is a basic example of how to use Select by Attribute using arcpy. This will also give
the total number of rows that meet the condition using arcpy.GetCount_management.

NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.
===============================================================================
"""

def Resident(students_path,student_fc):
    arcpy.env.workspace=students_path
    query_Y="RESIDENT = 'Y'"
    resident=arcpy.management.SelectLayerByAttribute(student_fc,"NEW_SELECTION",query_Y)
    total_resident=int(arcpy.GetCount_management(resident).getOutput(0))
    arcpy.AddMessage(f'Total number of students where RESIDENT = Y: {total_resident}')
