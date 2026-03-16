Please, can you help me to update the python script. 

/home/andrew/Code/andrew-seaford.co.uk/docs/freecad/darts-stand/dartStandTopAndBottonRail.py

- The script create a 3d dart stand in freecad. 
- The dart stand has a base plate rail, with letters attached to the plate. 
- There are holes from the top of the letters for holding the darts.

make the following changes:

1. Add a top plate. Similar to the "# 4. Create Base Plate based on the NEW footprint", create a plate that is above the letters. The top of the letters should touch the bottom of the top plate.

2. Change the number of holes in the section "# 5. HOLE CALCULATIONS" currently the script create a hole in every letter.

- Change the script to 3 holes. hopefully changing text_content to a fixed 3 in `step = plate_width / len(text_content)` will help.
- The 3 holes should be evenly spaces along the top rail.

