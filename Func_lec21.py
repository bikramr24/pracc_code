from loguru import logger

def calculate_fencing_cost(length,breadth,cost_per_ft):
    circumference = 2 * (length+breadth)
    cost_for_fencing = circumference * cost_per_ft
    return cost_for_fencing
def grass_plantation_cost(length,breadth,cost_per_sqft):
    area = 2 * (length * 10 + (breadth - 40) * 10) 
    cost_for_grass_plantation = area * cost_per_sqft
    return cost_for_grass_plantation

home = calculate_fencing_cost(100,0,17)
logger.info(f"cost of fencing for home :{home} ")
garden = calculate_fencing_cost(20,20,17)
logger.info(f"cost of fencing for garden :{garden} ")
pool = calculate_fencing_cost(10,20,17)
logger.info(f"cost of fencing for pool :{pool} ")
grass = grass_plantation_cost(100,100,10)
logger.info(f"cost of planting grass :{grass} ")