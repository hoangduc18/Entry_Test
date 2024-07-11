from datetime import datetime
import json
import pandas as pd
import pyodbc


filePath = r'D:\Learning\Learning2024\Entry_Test\Q3\employees.json'
with open(filePath) as file:
    datas = json.load(file)

for data in datas:
    data['join_date'] = datetime.strptime(data['join_date'], '%Y-%m-%d').date()

df = pd.DataFrame(datas)

db_connection = {
    'driver': '{SQL Server}',
    'server': 'WANGDUCK',
    'database': 'Entry_Test',
    'uid': 'sa',
    'pwd': '123456'
}

conn = pyodbc.connect(**db_connection)

cursor = conn.cursor()
cursor.execute(" CREATE TABLE employees ( id INT PRIMARY KEY,name TEXT, department TEXT, salary INT, join_date DATE)")

conn.commit()
conn.close()