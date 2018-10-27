import sqlite3

#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

couty = str(input('縣市'))
township = str(input('鄉鎮區'))
sqlstr = str(couty + '%' + township)

cursor = c.execute("SELECT * FROM hospitals WHERE address LIKE '" + sqlstr + "%' ")  #執行SQL

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()


conn.close()
