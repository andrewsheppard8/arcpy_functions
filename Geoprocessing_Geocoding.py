"""
===============================================================================
Script Name:       Geocoding using Arcpy
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
Basics of using Arcpy to geocode.

NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.

===============================================================================
"""

import arcpy
from arcpy import env

#Geocoding function. Note that the zip_field is optional, when used as a stand alone tool in a Toolbox in ArcGIS Pro. 
def Geocode(geodatabase,feature_class,locator,optional_field):
    arcpy.env.workspace=geodatabase
    table=f"TABLE_{feature_class}"
    optional_field = optional_field.replace(' ', '_')#remove spaces
    arcpy.AddMessage(optional_field)
    field_mapping = (
        "\'Address or Place\' {*address_field} VISIBLE NONE;Address2 <None> VISIBLE NONE;Address3 <None> VISIBLE NONE;"
        "Neighborhood <None> VISIBLE NONE;City <None> VISIBLE NONE;Subregion <None> VISIBLE NONE;"
        f"Region <None> VISIBLE NONE;\'ZIP\' {optional_field} VISIBLE NONE;ZIP4 <None> VISIBLE NONE;"
        "Country <None> VISIBLE NONE"
    )#*The address field was hardcoded here, but could be set dynamically
    arcpy.AddMessage("Geocoding with the following field mapping:")
    arcpy.AddMessage(field_mapping)
    
    arcpy.GeocodeAddresses_geocoding(
        in_table=table,
        address_locator=locator,
        in_address_fields=field_mapping,
        out_feature_class=feature_class,
        out_relationship_type="STATIC"
    )
    arcpy.AddMessage('Geocode complete')
