from loguru import logger

# CREATING LIST
labour_with_cost = {"Mahesh":500,"Mithilesh":400,"Ramesh":400,"Sumesh":300}
# logger.info(labour_with_cost)

# UPDATING LIST
labour_with_cost["JagMohan"] = 1000
labour_with_cost["Rampyare"] = 800
labour_with_cost["Mahesh"] = 600

# logger.info(labour_with_cost.keys())
# logger.info(labour_with_cost.values())
# logger.info(labour_with_cost.items())

# for keys in labour_with_cost:
    # logger.info(keys)
    # logger.info(labour_with_cost[keys]) this iterates values\


# data = {"employees":{"employee":[{"id":"1","firstName":"Tom","lastName":"Cruise","photo":"https://jsonformatter.org/img/tom-cruise.jpg"},{"id":"2","firstName":"Maria","lastName":"Sharapova","photo":"https://jsonformatter.org/img/Maria-Sharapova.jpg"},{"id":"3","firstName":"Robert","lastName":"Downey Jr.","photo":"https://jsonformatter.org/img/Robert-Downey-Jr.jpg"}]}}

# for i in range(len(data["employees"]["employee"])):
#     print(data["employees"]["employee"][i]["id"])
# count = 0

# prac_set = {"company":{"id" : 100, "name":"TechNova","founded":2015,"isActive":True,"address":{"street":"21 Silicon Avenue","city":"Bangalore","state":"Karnataka","country":"India","postalCode":560001},"departments":[{"id":101,"name":"Engineering","budget":1500000,"manager":{"id":1,"name":"Arjun Mehta","email":"arjun@technova.com"},"employees":[{"id":11,"name":"Riya Sharma","role":"Backend Developer","skills":["Python","SQL","Docker"],"salary":1200000,"isRemote":False},{"id":12,"name":"Karan Verma","role":"Data Engineer","skills":["Python","Spark","Airflow"],"salary":1400000,"isRemote":True}]},{"id":102,"name":"Marketing","budget":500000,"manager":{"id":2,"name":"Sneha Kapoor","email":"sneha@technova.com"},"employees":[{"id":21,"name":"Aman Singh","role":"SEO Specialist","skills":["SEO","Analytics"],"salary":600000,"isRemote":True}]}],"clients":[{"id":"C001","name":"Flipkart","contractValue":2500000,"isInternational":False},{"id":"C002","name":"Amazon","contractValue":5000000,"isInternational":True}],"products":[{"id":"P01","name":"DataFlow","version":"1.4.2","releaseDate":"2023-08-15","features":["ETL","Monitoring","Scheduling"],"isDeprecated":False},{"id":"P02","name":"InsightAI","version":"2.1.0","releaseDate":"2024-02-10","features":["Prediction","Visualization"],"isDeprecated":"abc"}]}}

# for i in range(len(prac_set["company"]["departments"])):
#     for j in range(len(prac_set["company"]["departments"][i]["employees"])):
        # logger.info(
        #     f"Salary : {prac_set["company"]["departments"][i]["employees"][j]["salary"]}"
        #     )
        # logger.info(
        #     f"Salary : {prac_set["company"]["departments"][i]["employees"][j]["isRemote"]}"
        #     )
        # if prac_set["company"]["departments"][i]["employees"][j]["isRemote"]:
        #     logger.info(f"name {prac_set["company"]["departments"][i]["employees"][j]["name"]}")
            
# for i in range(len(prac_set["company"]["departments"])):
#     for j in range(len(prac_set["company"]["departments"][i]["employees"])):
        
#         if prac_set["company"]["departments"][i]["employees"][j]["isRemote"]:
            
#             logger.info(
#                 prac_set["company"]["departments"][i]["employees"][j]["name"]
#             )
     
# assignment
total_cost = 0
mandate_days = 50
absent_days = {"Mahesh":3,"Mithilesh":0,"Ramesh":0,"Sumesh":0,"JagMohan" : 7, "Rampyare": 0}
for key in labour_with_cost:
    print(f"Cost for {key} is {(mandate_days - absent_days[key]) * labour_with_cost[key]}")
    total_cost = total_cost + (mandate_days-absent_days[key]) * labour_with_cost[key]
logger.info(f"total cost is {total_cost}")