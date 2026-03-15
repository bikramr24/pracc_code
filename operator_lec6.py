import sys
from loguru import logger
length_of_land = 100
breadth_of_land = 80
bricks_cost_per_piece = 10.5
labours_mistry = "Jaggu"
is_home = True

#Calculate total area of land
total_area_of_land = length_of_land * breadth_of_land
#BODMAS RULE
perimeter_of_land = 2* (length_of_land + breadth_of_land)

logger.info(f"total area of land is {total_area_of_land} sq.ft")
logger.info(f"perimeter of land is {perimeter_of_land} ft")
