import sys
from loguru import logger

length_of_land = int(input("Enter length :"))

if (length_of_land < 100):
    logger.info("Invalid, enter greater than 100 ")
    length_of_land = int(input("Enter length :"))
    if(length_of_land > 80):
        logger.info("You can plan a 3 bhk instead of 4")
elif (length_of_land > 500):
    logger.info("Area too big, you can build more than 2 houses")        
breadth_of_land = int(input("Enter breadth : "))

if (breadth_of_land < 40):
    logger.info("Invalid, enter greater than 40 ")
    breadth_of_land = int(input("Enter breadth :"))

bricks_cost_per_piece = int(input("Enter bricks per price :"))
labours_mistry = int(input("Enter labour mistry cost :"))
is_home = True
putput = lambda x,y : "True" if x >= y else "False"
logger.info(putput(5,3))
logger.info(f"{length_of_land}")
logger.info(f"{breadth_of_land}")
logger.info(f"{bricks_cost_per_piece}")
logger.info(f"{labours_mistry}")

