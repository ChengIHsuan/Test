import sqlite3

#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

county = str(input('縣市'))
township = str(input('鄉鎮區'))

i = county.find("北")
if i != -1:
    area = str("_北%" + township)
else:
    area = str('%' + county + '%' + township)

cursor = c.execute("""
SELECT h.*, AVG(d.hospital_score) FROM raw_data as d
JOIN hospitals as h ON d.hospital_id = h.id 
WHERE h.address LIKE '""" + area + """%' 
GROUP BY d.hospital_id 
        """)  #執行SQL

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()

conn.close()
