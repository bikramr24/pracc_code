import sys
from loguru import logger

labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh", 500, 500, 400, 400, 600]
logger.info(labour_name[1:])
logger.info(labour_name[0:2])
logger.info(labour_name[0:8:2])

# # REVERSING A LIST
logger.info(labour_name[::-1])

# new_labour = ["Ram","Mohan"]

# labour_name.append(new_labour)

logger.info(labour_name)
labour_name.insert(4,"Jaggu")
labour_name.append(600)

# labour_name.insert(5,new_labour)

# labour_name  = labour_name + new_labour
# logger.info(labour_name)


wage = labour_name.pop()
print(wage)

if wage >= 500:
    print("costly")
else:
    print("not costly")

labour_name.remove(500)
logger.info(labour_name)

# del labour_name

# ----
# CHANGING LIST VALUES
labour_name_CP = ["Maheh","Rameh","Mithileh","Sumsh", 500, 50, 400, 400, 600]
logger.info(labour_name_CP)

labour_name_CP[5] = 500
logger.info(labour_name_CP)

labour_name_CP[0:4] =["Mahesh","Ramesh","Mithilesh","Sumesh"]
logger.info(labour_name_CP)

# SPLIT USE CASE
api_endpoint = "https://dev.azure.com/{organization}/{project}/_apis/serviceendpoint/endpoints?api-version=7.1"
new_apilist = api_endpoint.split("/")
print(new_apilist)
print(new_apilist[-1])
print(new_apilist[-2])



