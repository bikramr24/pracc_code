from loguru import logger

name = "bikram rewani"
counter = 0
# for char in name:
#     logger.info(f"{counter},{char}")
#     counter +=1

# logger.info(chr(65))
# logger.info(ord("a"))
# logger.info(ord("z"))
# logger.info(ord("A"))
# logger.info(ord("Z"))

# logger.info(name[0:4])
# logger.info(name.capitalize())
# logger.info(name.count("a"))
# logger.info(name.endswith("ani"))
# logger.info(name.islower())
# name_new = name.replace("bikram","  RoHaN")
# logger.info(name_new)
# logger.info(len(name_new))
# logger.info(name_new.strip())
# logger.info(len(name_new.strip()))

# Q1

# string = "Programming Asan Hai"
# new_string = ""
# for chr in string:
#     if chr.islower() == True:
#         new_string = new_string + chr.upper()
#     else:
#         new_string = new_string + chr.lower()

# logger.info(new_string)

# name = "raghu ram rajan banerjee"
# names = name.split(" ")
# logger.info(names)

# #Q2

# phone = ['90908778','78567365577','67453489219']
# emails = [
#     "sarah.mitchell@techcorp.com",
#     "jdoe1985@gmail.com",
#     "alex.rivera@startup.io",
#     "maria.santos@university.edu",
#     "ryan.k.thompson@consulting.net"
# ]

# new_phone = []
# for item in phone:
#     item = item.strip()
#     a = len(item.strip())
#     new_phone = new_phone + [item[0] + "*" * (a-2) + item[a-1]]
# print(new_phone)

# new_emails = []
# for item in emails:
#     item = item.strip()
#     item_l = (item.strip()).split("@")
#     a = len(item_l[0])
#     new_emails = new_emails + [(item_l[0])[0] + "*" * (a-2) + (item_l[0])[a-1] +"@" + item_l[1]]
# print(new_emails)



# Q3
input = ["/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2/file_path/teams/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path/teams/bin/test1.csv",
"/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22/file_path/data/bin/test1.csv",
"/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2/file_path//usr/bin/test1.csv",
"/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28/file_path//usr/bin/test1.csv",
"/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31/file_path/worklog/bin/test1.csv",
"/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2/file_path//tmp/bin/test1.csv"
]

new_ip = []
cleaned_ip = []
unique_ip = []
for item in input:
    new_ip = new_ip + item.split("/")
    for item in new_ip:
        if item.startswith("10."):
           cleaned_ip = cleaned_ip + [item]
        else:
            new_ip.remove(item)
for ip in cleaned_ip:
    if ip not in unique_ip:
        unique_ip = unique_ip + [ip]
    else:
        continue

print(unique_ip)       

