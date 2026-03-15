import sys
length_of_land = 190
breadth_of_land = 190
bricks_cost_per_piece = 10.5
labours_mistry = "Jaggu"
is_home = True

print("home is '4bhk' \nlength of land :",length_of_land)
print("breadth of land :",breadth_of_land)
print("labours mistry {}".format(labours_mistry))
print(f"bricks cost :{bricks_cost_per_piece}")
print('''triple 
quotation, usage 
here''')

# logging
from loguru import logger
import logging
logging.basicConfig(level = logging.DEBUG, format= '%(asctime)s %(message)s  %(filename)s:%(lineno)d')
logging.info(f"bricks cost :{bricks_cost_per_piece}")

#advanced printing
# logger.add(sys.stderr, 
#            format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
#                   "<level>{level: <8}</level> | "
#                   "<cyan>{file}</cyan>:<magenta>{line}</magenta> | "
#                   "<level>{message}</level>",
#            level="DEBUG",
#            colorize=True)

 
logger.info(f"bricks cost :{bricks_cost_per_piece}")
# print(id(length))shows 
# actual allocated location on RAM
# print(length_of_land,breadth_of_land,bricks_cost_per_piece,labours_mistry,is_home)
# print(type(length_of_land),type(breadth_of_land),type(bricks_cost_per_piece),type(labours_mistry),type(is_home))