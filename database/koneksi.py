
import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="belajargrpc"
)
cursor=db.cursor()
sql="SELECT*FROM users"
cursor.execute(sql)
result=cursor.fetchall()
for x in result:
    print(x)