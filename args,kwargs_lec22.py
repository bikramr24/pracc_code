from loguru import logger
import os
print(os.getcwd())  # This shows you where log.txt is being saved

def final_cart_amount(*args,discount = 0.1):
    cart_amount  = 0
    for item in args:
        cart_amount += item    
    discounted_cart_value = cart_amount - (cart_amount * discount)
    logger.info(f"original bill :{cart_amount}")
    return discounted_cart_value

shop = final_cart_amount(1000,2000,5000,8000)
logger.info(f"discounted bill :{shop}")

def sum_of_n(*args):
    sum = 0
    for item in args:
        sum += item
    return sum    

want_sum = sum_of_n(5,7,8,10,20,30)
logger.info(f"sum is : {want_sum}")

def generic_logging(**kwargs):
    with open(r"F:\MKPython Saves\Var\logs.txt","a") as f:
            line = ",".join(f"{key},{value}" for key,value in kwargs.items())
            f.write(f"{line}\n")        

user1 = generic_logging(status = "failed", status_code = 500, error = "Table not found")
user1 = generic_logging(status = "passed", status_code = 200, message = "Table updated")
user1 = generic_logging(status = "failed", status_code = 404, message = "server error")