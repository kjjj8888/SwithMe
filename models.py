import pymysql

db = pymysql.connect(host='127.0.0.1', 
                     user='root', 
                     password='0000', 
                     db='corpDB4', 
                     charset='utf8mb4')

cursor = db.cursor()

sqlmain = "select * from main;"
cursor.execute(sqlmain)

data_list = cursor.fetchall()

sqlqualify1 = "select * from main where idx = 1;"
cursor.execute(sqlqualify1)
idx1=cursor.fetchall()

sqlqualify2 = "select * from main where idx = 2;"
cursor.execute(sqlqualify2)
idx2=cursor.fetchall()

sqlqualify3 = "select * from main where idx = 3;"
cursor.execute(sqlqualify3)
idx3=cursor.fetchall()

sqlqualify4 = "select * from main where idx = 4;"
cursor.execute(sqlqualify4)
idx4=cursor.fetchall()

sqlqualify5 = "select * from main where idx = 5;"
cursor.execute(sqlqualify5)
idx5=cursor.fetchall()

sqlqualify6 = "select * from main where idx = 6;"
cursor.execute(sqlqualify6)
idx6=cursor.fetchall()

sqlqualify7 = "select * from main where idx = 7;"
cursor.execute(sqlqualify7)
idx7=cursor.fetchall()

sqlqualify8 = "select * from main where idx = 8;"
cursor.execute(sqlqualify8)
idx8=cursor.fetchall()

sqlqualify9 = "select * from main where idx = 9;"
cursor.execute(sqlqualify9)
idx9=cursor.fetchall()

sqlqualify10 = "select * from main where idx = 10;"
cursor.execute(sqlqualify10)
idx10=cursor.fetchall()

sqlqualify11 = "select * from main where idx = 11;"
cursor.execute(sqlqualify11)
idx11=cursor.fetchall()






