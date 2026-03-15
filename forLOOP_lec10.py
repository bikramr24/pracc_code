# import sys
# from loguru import logger

# labour_names = ["Mahesh","Ramesh","Mithilesh","Sumesh","Suresh","Rinku"]
# # for name in labour_names:
# #     logger.info(f"Labour name is : {name}")

# for number in range(len(labour_names)):
#     logger.info(f"labour {number+1} is {labour_names[number]}")

# # n = int(input("Enter a number : "))

# # for number in range(1,n+1):
# #     line = "* "* (number)
# #     print(line.rstrip())

# for number in range(2,101, 2):
#     print(number)

#codex
n = 5

for i in range(n, 0,-1):
    line = " *" * i
    print(line.lstrip())

