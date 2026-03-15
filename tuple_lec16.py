from loguru import logger

# test_tuple = (1,2,45,65,32,"True","Manish",True)

# logger.info(test_tuple)
# logger.info(test_tuple[4:7])
# logger.info(type(test_tuple))

# if 1 in test_tuple:
#     logger.info("hurray")

# # test_tuple[2] = 45 Assignment error 
# logger.info(test_tuple[2])

# new_tuple = (2,)
# logger.info(type(new_tuple))

#Q 1
test_tuple1 = ([5,6],[6,7,8,9],[3])
# output = (5,6,6,7,8,9,3)
new_tup = ()
for item in test_tuple1:
    new_tup = new_tup + tuple(item)
logger.info(new_tup)

#Q 2
tuple1 = (10,2,3,5)
tuple2 = (3,6,4,3)

tuple3= ()

for i in range(len(tuple2)):
    result = (tuple1[i]) ** (tuple2[i])
    tuple3 = tuple3 + (result,)
logger.info(tuple3)