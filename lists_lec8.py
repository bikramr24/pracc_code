# import sys
# from loguru import logger

# labour_details = ["Mahesh","Ramesh","Mithilesh","Sumesh","Suresh","Rinku"]
# logger.info(f"first element in the list is : {labour_details[2]}")
# logger.info(f"first element in the list is : {labour_details[-2]}")

# # labour_details.append("Ram")
# # logger.info(f"first element in the list is : {labour_details}")

# labour_details.insert(0,"Ram")
# labour_details.insert(4,"Manoj")
# logger.info(f"first element in the list is : {labour_details}")

# new_labours = ["MoniRam", "MikaRam"]
# labour_details.extend(new_labours)
# logger.info(f"first element in the list is : {labour_details}")

# MULTIDIMENSIONAL LIST
#2D One Layer
labour_with_cost = [["Mahesh",500 ], ["Ramesh", 400],["Mithilesh",400], ["Sumesh",300]]


# 3D list (2x2x2 cube)
cube = [
    [[1, 2], [3, 4]], [[5, 6], [7, 8]]
]

print(cube[1][1][0])  # 3