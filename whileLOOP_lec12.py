import sys
import time
from loguru import logger

labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

name_iter = 0 

while (name_iter < len(labour_name)):
    logger.info(labour_name[name_iter])
    time.sleep(3)
    name_iter += 1

#REVERSE WHILE

name_iter = len(labour_name) - 1

while (name_iter >= 0):
    logger.info(labour_name[name_iter])
    time.sleep(4)
    name_iter -= 1

# REVERSED WHILE LOOP USING -VE INDEX

name_iter = -1

while (name_iter >= -(len(labour_name))):
    logger.info(labour_name[name_iter])
    time.sleep(5)
    name_iter = name_iter - 1

