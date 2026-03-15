from loguru import logger
names = ["manish", "nilesh", "ram"]

final_result =" "
for name in names:
    # final_result += name
    final_result = " ".join(names)
    logger.info(final_result)
logger.info(final_result)

paths = [
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.2",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.156.2",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2",
    "/region/japan/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.22",
    "/region/india/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.167.2",
    "/region//us-east-a/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.179.28",
    "/region//us-east-b/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.155.31",
    "/region//us-east-c/north/resource/vminsatnce/subsid/ae-456-df/server/10.168.151.2"
]

unique_ips = list(dict.fromkeys(path.split("/")[-1] for path in paths))

print(unique_ips)