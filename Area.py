import sqlite3

#connect database
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

couty = str(input('縣市'))
township = str(input('鄉鎮區'))
area = str(couty + '%' + township + '%')

cursor = c.execute("SELECT * FROM hospitals WHERE address LIKE '" + area + "'")  #執行SQL

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()

conn.close()
