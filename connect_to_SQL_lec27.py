from loguru import logger
import mysql.connector


connection = mysql.connector.connect(host = "localhost",user = "root", password = "Bikram@DE#$%^",auth_plugin="mysql_native_password")
logger.info(f"{connection}")

cursor = connection.cursor()
# cursor.execute("select name,wages from mydatabase.labours_table")

# insert_query = "INSERT INTO mydatabase.labours_table (id,name, role, wages) VALUES (%s, %s, %s)"
# insert_query = "UPDATE mydatabase.labours_table SET id = %s where id = %s)"
insert_query = "delete from mydatabase.labours_table where id =8"
cursor.execute(insert_query)

# result = cursor.fetchall()
# logger.info(f"{result}")

connection.commit()
connection.close()
cursor.close()