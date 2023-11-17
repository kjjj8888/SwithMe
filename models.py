import pymysql

db = pymysql.connect(host='127.0.0.1', 
                     user='root', 
                     password='0000', 
                     db='testdb', 
                     charset='utf8')

def test():
    cursor = db.cursor()

    sql = "select * from testtable;"
    cursor.execute(sql)
    result = cursor.fetchall()
    db.close()

    return len(result)







