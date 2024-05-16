# Tools for OpenMower
## Split a map

To be used with Openmower GUI using backup and restore functionality.

Useful when there are more areas and you want to "jump" to a specific area directly, i.e. not to use "Mow next area" functionality.

A map with M mowing areas and N navigation areas will be split into:
- M files, where file number X contains:
  - Mow area number X 
  - The existing N navigation area + the other (M-X) mowing areas transformed as navigation areas
     - the idea of transforming the other mowing areas into navigation areas is because the mower does not start if it's outside of them, so it's useful to fill the space with navigation areas.

### Workflow:
- backup a map as a JSON file (e.g. map.json)
- run ```python split_map_areas.py map.json```
- the result is a number of files (the number of mowing areas) each with name "split_area**X**_from_map.json", where **X** is the index from 0 to the number of mowing areas 
  - the location of the output files is the same as the input files
- if you want to mow directly area X, Restore the file "split_areaX_from_map.json"
- do not forget to press "Save Map"

### Example of usage:

```
> python3 split_map_areas.py maps/area0_1_2_3_4_5_6_edit8.json

Input map file:  maps/area0_1_2_3_4_5_6_edit8.json
Creating map for area 0
 Output file: maps/split_area0_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 1
 Output file: maps/split_area1_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 2
 Output file: maps/split_area2_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 3
 Output file: maps/split_area3_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 4
 Output file: maps/split_area4_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 5
 Output file: maps/split_area5_from_area0_1_2_3_4_5_6_edit8.json

Creating map for area 6
 Output file: maps/split_area6_from_area0_1_2_3_4_5_6_edit8.json
```
**Before:**

<img width="619" alt="image" src="https://github.com/lucianleahu/openmower-tools/assets/16760872/c07b933e-d387-4c4c-a117-b784c4aeaa06">

**After:**

- area 0:
  <img width="601" alt="image" src="https://github.com/lucianleahu/openmower-tools/assets/16760872/c230ffd2-3ff6-4dbb-9f90-d5e138fe6232">

- area 4:
  <img width="604" alt="image" src="https://github.com/lucianleahu/openmower-tools/assets/16760872/c6f07c25-3576-40f3-afac-9fa5443b1f4b">




