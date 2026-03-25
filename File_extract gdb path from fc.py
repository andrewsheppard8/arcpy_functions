"""
===============================================================================
Script Name:       Extract Path for GDB from Feature Class
Author:            Andrew Sheppard
Role:              GIS Solutions Engineer
Email:             andrewsheppard8@gmail.com
Date Created:      2026-03-23

Description:
-------------
How take a path for a feature class and pull the gdb path, which can be used
later as a global variable.
===============================================================================
"""

gdb_path = None
def extract_gdb_path(tracts):
    global gdb_path
    # Split path into parts
    parts = tracts.split('/')
    for i, part in enumerate(parts):
        if part.endswith('.gdb'):
            # Join parts back to get the full .gdb path
            gdb_path = '/'.join(parts[:i+1])  # Corrected line
            break

