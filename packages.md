# Building packages


## My new project

1. When you create a package for a new project, think first what existing libraries you can use,
    and which to extend to fit your needs.
1. Any reasonably generalizable code should be moved to another repo, 
    like `workflow_tools`, `gis_utils`, `gpt_chains`, etc.

## Dependencies

1. Use SNAP workflows as much as possible (and keep them in `gpt_chains`). 
    They have proven to be reliable and efficient.
1. Use the modern `rasterio` and `fiona` instead of the old `gdal` and `ogr` Python bindings.
