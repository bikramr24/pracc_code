import sys
from loguru import logger

# # question_text = ''' Ralph Kimball founded the Kimball Group. Since the mid-1980s, he has been the 
# # data warehouse and business intelligence industry’s thought leader on the dimen
# # sional approach. He has educated tens of thousands of IT professionals. The Toolkit 
# # books written by Ralph and his colleagues have been the industry’s best sellers 
# # since 1996. Prior to working at Metaphor and founding Red Brick Systems, Ralph 
# # coinvented the Star workstation, the fi rst commercial product with windows, icons, 
# # and a mouse, at Xerox’s Palo Alto Research Center (PARC). Ralph has a PhD in 
# # electrical engineering from Stanford University'''

# # # convert into list 
# # question_list = (question_text.lower()).split(" ")
# # print(question_list)

# # counter = 0

# # for item in question_list:
# #     if item == "the":
# #         counter += 1

# # logger.info(f"The is {counter} times")

# list = [5,8,69,89,108,700,999]

# number_to_insert = 100
# count = 0

# for number in list:
#     if number < number_to_insert:
#         count += 1
#     else:
#         break

# list.insert(count, number_to_insert)
# logger.info(str(count), list)
# logger.info(list)

# number_to_insert = 100 

# lst = [5,18,77,108,930]
# index = 0
# for number in lst:
#     if number > number_to_insert:
#         index = index
#         break
#     else:
#         index = index + 1
# logger.info(index)

# lst.append(None)

# logger.info(lst)
# for number in range (len(lst)-1,index,-1):
#     lst [number] = lst [number - 1]

# logger.info(lst)

# lst[index] = number_to_insert
# logger.info(lst)

list2 = [202,165,89,76,12]
number_to_insert2 = 90

index = 0
old_len = len(list2)
for number in list2:
    if number > number_to_insert2:
        index = index + 1
    else:
        index = index
        break
logger.info(f"{index} is index value")

if index == 0:
    extra = [None]
    extra[0] = number_to_insert2 
    list2 = extra + list2
    print("ring",list2)
elif index == old_len:
    extra = [None]
    extra[0] = number_to_insert2 
    list2 = list2 + extra
    print("ring ring ", list2)
else:
    list2.append(None)

    for number in range(len(list2)-1 ,index,-1):
        list2 [number] = list2 [number - 1]

    logger.info(list2)

    list2[index] = number_to_insert2
    logger.info(list2)