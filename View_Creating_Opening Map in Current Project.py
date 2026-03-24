"""
===============================================================================
Script Name:       Creating/Opening a Map in a Project
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
1. Will check to see if a map with a name of map_name exists in the open project.
2. Will open the map in the current aprx.

NOTE: These were part of a larger script and are not guarenteed to work out of the box.
        See Script "Geocoding from Excel.py" in arcpy_scripts repo for details.
===============================================================================
"""
#function 1
def ensure_map_exists(map_name):
    aprx_path='CURRENT'
    aprx=arcpy.mp.ArcGISProject(aprx_path)
    for map_obj in aprx.listMaps(map_name):
        aprx.deleteItem(map_obj)
        arcpy.AddMessage(f"{map_name} map exists, deleted")
    map_obj = aprx.createMap(map_name)
    arcpy.AddMessage(f"{map_name} map created")

    return map_obj

#function 2
def set_active_view(map_name):
    aprx_path = 'CURRENT'
    aprx = arcpy.mp.ArcGISProject(aprx_path)
    map_view = aprx.listMaps(map_name)[0]
    map_view.openView()
    arcpy.AddMessage(f"Set {map_name} as the active view")
