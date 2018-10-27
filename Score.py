import sqlite3

#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

#couty = str(input('縣市'))
#township = str(input('鄉鎮區'))
#sqlstr = str(couty + '%' + township)

cursor = c.execute("""
SELECT h.*, AVG(d.hospital_score) FROM raw_data as d
INNER JOIN hospitals as h
WHERE d.hospital_id = h.id 
group by d.hospital_id
        """)  #執行SQL

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()

conn.close()
