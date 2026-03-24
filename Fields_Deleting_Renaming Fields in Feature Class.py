"""
===============================================================================
Script Name:       Deleting/renaming fields in feature class
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-24

Description:
-------------

This script shows a pattern for cleaning fields in a feature class.
===============================================================================
"""

def CleanFields(output_fc):
    fields_to_del = []
    field_List = [field.name for field in arcpy.ListFields(output_fc)]
    for field_name in field_List:
        if field_name in ["HARDCODED LIST OF FIELDS THAT YOU WANT TO DELETE"]:
            fields_to_del.append(field_name)
            arcpy.AddMessage(f'{field_name} will be deleted')
    fields_to_delete=[field for field in field_List if field in fields_to_del]
    fields_to_delete_str = ";".join(fields_to_delete)
    for field in fields_to_delete:
        arcpy.DeleteField_management(output_fc, fields_to_delete_str)
        arcpy.AddMessage(f'{field} deleted')
    fields=arcpy.ListFields(output_fc)
    user_status_found=False
    user_stutype_found=False
    for field in fields:
        if field.name.lower()=="FIELD_NAME".lower():
            status_name=field.name.replace("FIELD_NAME","NEW_NAME")
            new_alias="Stutype1"
            arcpy.AlterField_management(output_fc,field.name,status_name,new_alias)
            arcpy.AddMessage(f'{field.name} renamed to {status_name}')
            user_status_found=True
        elif field.name.startswith("USER_"): #how to batch rename fields
            new_name=field.name.replace("USER_","")
            arcpy.AlterField_management(output_fc, field.name, new_name)
            arcpy.AddMessage(f'{field.name} renamed to {new_name}')
    arcpy.AddMessage('Fields removed and renamed')

output_fc=arcpy.GetParameterAsText(0)
CleanFields(output_fc)
