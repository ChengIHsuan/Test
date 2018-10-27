import sqlite3
#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

dis = str(input("特殊疾病"))
getId = c.execute("SELECT id FROM diseases WHERE name LIKE '%" + dis + "%'")
diseaseId = str(getId.fetchone()[0])
str = {
    '1': "SELECT h.name, f.h_1, f.h_2, f.h_3, f.h_4, f.h_5 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '2': "SELECT h.name, f.h_6, f.h_7, f.h_8, f.h_9, f.h_10, f.h_11 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '3': "SELECT h.name, f.h_12, f.h_13, f.h_14, f.h_15 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '4': "SELECT h.name, f.h_16, f.h_17 f.h_18 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '5': "SELECT h.name, f.h_19, f.h_20, f.h_21, f.h_22 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '6': "SELECT h.name, f.h_23, f.h_24, f.h_25, f.h_26, f.h_27 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '7': "SELECT h.name, f.h_28, f.h_29, f.h_30, f.h_31 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id",
    '8': "SELECT h.name, f.h_32, f.h_33 FROM hospitals h JOIN final_data f ON h.id = f.hospital_id"
}
sqlstr = str.get(diseaseId)
cursor = c.execute(sqlstr)

row = cursor.fetchone()
if row is None:
  print("找不到您要的資料訊息")
while row is not None:
   print(row)
   row = cursor.fetchone()

conn.close()