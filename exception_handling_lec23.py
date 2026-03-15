from loguru import logger

# def final_cart_amount(*args,discount = 0.1):
#     try:
#         cart_amount  = 0
#         for item in args:
#             cart_amount += item
#         discounted_cart_value = cart_amount - (cart_amount * discount)
#         logger.info(f"original bill :{cart_amount}")
#         return discounted_cart_value
#     except TypeError as e:
#         logger.info("Please enter value in integer")
#         # raise e(just raise also works)
#         raise Exception("value is not integer coming from type error")from e
#     except NameError as e:
#         logger.info("Please check variable names")
#         # raise e(just raise also works)
#         raise Exception("variable name might not be correct")from e
#     except Exception as e:
#         logger.info("Cannot process cart amount",e)
#         raise e
# try:    
#     shop = final_cart_amount(5.91000,'2000',5000,8000,10000,discount = 0.35)
#     logger.info(f"discounted bill :{shop}")
# except Exception as e:
#     logger.info(e)
#     raise


# final_cart_amount()
#     ↓
# TypeError occurs
#     ↓
# Caught in inner except
#     ↓
# Wrapped using "from e"
#     ↓
# Sent upward
#     ↓
# Caught in outer except
#     ↓
# Logged
#     ↓
# raise e
#     ↓
# Program crashes

import os
import logging
from loguru import logger

filepath = "f:/MKPython Saves/Var/emp.txt"

try:
    # Check if file is empty BEFORE opening O(1)
    if os.path.getsize(filepath) == 0:
        raise ValueError("File is empty")
    # Check if file is empty BEFORE opening O(n)
    with open(filepath, "r") as f:
        names = [line.strip() for line in f if line.strip()]
        
        if not names:  # File had only whitespace/newlines
            raise ValueError("File has no valid data")
            
    unique_names = set(names)
    logger.info(f"Unique names: {unique_names}")


except FileNotFoundError:
    logger.error("File may not exist")
    raise
    
except ValueError as e:
    logger.error(f"Error: {e}")
    raise
logger.info("done")
