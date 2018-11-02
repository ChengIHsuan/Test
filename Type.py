import sqlite3
#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

type = str(input("醫院層級"))

cursor = c.execute("""
SELECT h.*, AVG(d.hospital_score) FROM raw_data as d
JOIN hospitals as h ON d.hospital_id = h.id 
WHERE h.type = '""" + type + """' 
GROUP BY d.hospital_id 
        """)  #執行SQL

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()

conn.close()
