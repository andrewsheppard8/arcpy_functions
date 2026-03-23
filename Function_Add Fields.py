"""
===============================================================================
Script Name:       Adding fields in feature class using ArcPy
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

#Adding additional fields based on organization needs
def AddFields(geodatabase,feature_class):
    arcpy.env.workspace=geodatabase
    #fields to be added/checked
    field_infos = [
        ('RESIDENT', 'TEXT', 1),
        ('STUTYPE', 'TEXT', 2),
        ('GRADE', 'SHORT', None),
        ('CODE', 'SHORT', None),
        ('NAME', 'TEXT', None)
        ]
    existing_fields = [field.name for field in arcpy.ListFields(feature_class)]
    for field_name, field_type, field_length in field_infos:
        if field_name not in existing_fields:
            arcpy.AddField_management(feature_class, field_name, field_type, field_length=field_length)
            arcpy.AddMessage(f"Added new field: {field_name}")
        else:
            arcpy.AddMessage(f'{field_name} already exists. Not added to feature class')

geodatabase=arcpy.GetParameterAsText(0)
feature_class=arcpy.GetParameterAsText(1)
AddFields(geodatabase,feature_class)


=======
"""
===============================================================================
Script Name:       Adding fields in feature class using ArcPy
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

#Adding additional fields based on organization needs
def AddFields(geodatabase,feature_class):
    arcpy.env.workspace=geodatabase
    #fields to be added/checked
    field_infos = [
        ('RESIDENT', 'TEXT', 1),
        ('STUTYPE', 'TEXT', 2),
        ('GRADE', 'SHORT', None),
        ('CODE', 'SHORT', None),
        ('NAME', 'TEXT', None)
        ]
    existing_fields = [field.name for field in arcpy.ListFields(feature_class)]
    for field_name, field_type, field_length in field_infos:
        if field_name not in existing_fields:
            arcpy.AddField_management(feature_class, field_name, field_type, field_length=field_length)
            arcpy.AddMessage(f"Added new field: {field_name}")
        else:
            arcpy.AddMessage(f'{field_name} already exists. Not added to feature class')

geodatabase=arcpy.GetParameterAsText(0)
feature_class=arcpy.GetParameterAsText(1)
AddFields(geodatabase,feature_class)
