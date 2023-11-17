import mysql.connector
import pandas as pd
import numpy as np
import html

# 해당 데이터베이스로 수정
conn = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="yourdatabase"
)

query = "SELECT * FROM table_name" # 테이블 이름으로 수정
df = pd.read_sql_query(query, conn)

for text in df['column_name']: # column 이름으로 수정
    start_index = text.find('항공기 SW개발')
    end_index = text.find('항공기 SW개발 끝')
    if start_index != -1 and end_index != -1:
        text = text[start_index:end_index]
        
        numbers = [float(s) for s in text.split() if s.isdigit()]

        changes = [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]

        average_change = np.mean(changes)
        std_change = np.std(changes)

        if average_change > std_change:
            result = '성장세'
        elif average_change < -std_change:
            result = '하락세'
        else:
            result = '안정세'

        with open('result.html', 'w', encoding='utf-8') as f:
            f.write(html.escape(result))

conn.close()
