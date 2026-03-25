"""
===============================================================================
Script Name:       Select by Location Query
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-25

Description:
-------------
This is a basic example of how to use Select by Location using arcpy

NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.
===============================================================================
"""

def SpatialJoin_Y(students_path,student_fc,district):
    arcpy.env.workspace=students_path
    in_district=arcpy.SelectLayerByLocation_management(student_fc, "WITHIN", district, "", "NEW_SELECTION")
    arcpy.CalculateField_management(in_district,"RESIDENT", "'Y'")
    arcpy.SelectLayerByAttribute_management(student_fc, "CLEAR_SELECTION")
