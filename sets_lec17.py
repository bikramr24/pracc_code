from loguru import logger

# set_variable = {1,2,7,8,4,12}
# logger.info(set_variable)

# # SETS ITERABLE
# # for number in set_variable:
# #     logger.info(number)
# new_set = {2,4,6,5,15}
# new1 = new_set
# logger.info(set_variable.union(new_set))
# logger.info(set_variable.intersection(new_set))
# logger.info(set_variable.difference(new_set))
# logger.info(new_set.difference(set_variable))
# logger.info(set_variable.symmetric_difference(new_set))
# logger.info(set_variable.isdisjoint(new_set))
# logger.info(set_variable.issubset(new_set))
# logger.info(set_variable.issuperset(new_set))
# set_variable.add(45)
# logger.info(set_variable)
# set_variable.update(new1)
# print(set_variable)

# Q1
list1 = [1,2,3,4,5,6]
list2 = [4,5,6,7,8]

s1 = set(list1)
s2 = set(list2)

logger.info(f"additional values list1 {list(s2.difference(s1))}" )
logger.info(f"missing values list1 {list(s1.difference(s2))})")
logger.info(f"additional values list2 {list(s1.difference(s2))}") 
logger.info(f"missing values list2 {list(s2.difference(s1))}")

# Q2
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80,100]
ar3 = [3,4,15,20,30,70,80,120]

s1 = set(ar1)
s2 = set(ar2)
s3 = set(ar3)
common = []
for item in ar1:
    if item in ar2 and item in ar3:
        common = common + [item]
logger.info(f"common in all 3 list is :{common}") 
logger.info((s1.intersection(s2)).intersection(s3))