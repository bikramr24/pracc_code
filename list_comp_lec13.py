from loguru import logger

list_numbers = [1,2,3,4,5,6,7,8,9,10,11,13,78,79]
new_list = []
# new_list =[2,4,6,8,10] OUTPUT
# LIST COMPREHENSION ONLY IF
new_list = [number for number in list_numbers if number % 2 == 0]
logger.info(new_list)

# LIST COMPREHENSION ONLY IF AND ELSE
new_list1 = ["even" if number % 2 == 0 else "odd" for number in list_numbers]
logger.info(new_list1)

