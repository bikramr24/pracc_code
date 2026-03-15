from loguru import logger
import configparser
config = configparser.ConfigParser()

config.read(r"F:\MKPython Saves\Var\config_file.ini")

bricks_cost = config["raw_materials"]["Bricks"]

logger.info(f"{bricks_cost},type of bricks_cost = {type(bricks_cost)}")

def total_no_of_bricks_R1(length,breadth,height):
    no_of_bricks_for_length = (length/0.833) * (height / 0.3)
    total_no_of_bricks_for_length = 2 * no_of_bricks_for_length

    no_of_bricks_for_breadth = (breadth/0.23) * (height / 0.3)
    total_no_of_bricks_for_breadth = 2 * no_of_bricks_for_breadth

    total_bricks_R1 = total_no_of_bricks_for_breadth + total_no_of_bricks_for_length
    return total_bricks_R1
def total_no_of_bricks_OTHERROOMS(length,breadth,height):
    no_of_bricks_for_length = (length/0.833) * (height / 0.3)
    total_no_of_bricks_for_length = 2 * no_of_bricks_for_length

    no_of_bricks_for_breadth = (breadth/0.23) * (height / 0.3)
    total_no_of_bricks_for_breadth = no_of_bricks_for_breadth

    total_bricks_otherR = total_no_of_bricks_for_breadth + total_no_of_bricks_for_length
    return total_bricks_otherR
def total_cost_for_bricks(config):
    bricks_cost = float(config["raw_materials"]["Bricks"])
    total_bricks_for_room1 = total_no_of_bricks_R1(15,20,10)
    total_no_of_bricks_oth_room = total_no_of_bricks_OTHERROOMS(15,20,10)
    final_cost = total_bricks_for_room1 * bricks_cost + 3 * total_no_of_bricks_oth_room * bricks_cost
    return final_cost

result = total_cost_for_bricks(config)
logger.info(f"bricks total cost for room: {result}")

# Q1:



def book_bill_new(student_details):
    books = 0
    book_bill = 0
    for key,value in student_details.items():
        for values in value:
            book_bill = book_bill + int(config["school_books"][f"{values}"])
            books = books + 1
        if books >= 2:
            book_bill = book_bill * 0.9
            logger.info(f"for student{key} book bill is {book_bill}")
        else:
            book_bill = book_bill
            logger.info(f"for student{key} book bill is {book_bill}")            
        book_bill = 0
        books = 0

student_details = {1:["Math","History"],2:["Biology","Chemistry"],3:["Science"]}    
book_bills = book_bill_new(student_details)