import sqlite3
#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

key1 = str(input("keyword1"))
key2 = str(input("keyword2"))
key3 = str(input("keyword3"))

try:
    getId= c.execute("SELECT id FROM category WHERE name = '" + key1 + "'")
    keyId1 = str(getId.fetchone()[0])
    print(keyId1 + "/1")
    getId = c.execute("SELECT id FROM category WHERE name  = '" + key2 + "'")
    keyId2 = str(getId.fetchone()[0])
    print(keyId2 + "/2")
    getId = c.execute("SELECT id FROM category WHERE name = '" + key3 + "'")
    keyId3 = str(getId.fetchone()[0])
    print(keyId3 + "/3")
    str = {
        '1': "f.h_3, f.h_6, f.h_7, f.h_10, f.h_11, f.h_20, f.h_21, f.h_22, f.h_23, f.h_24, f.h_26, f.h_27, f.h_32, f.h_33",
        '2': "f.h_12, f.h_13, f.h_14, f.h_15, f.h_25",
        '3': "f.h_30",
        '4': "f.h_1",
        '5': "f.h_2, f.h_4, f.h_8, f.h_18, f.h_31",
        '6': "f.h_5, f.h_9",
        '7': "f.h_16, f.h_17",
        '8': "f.h_19 ",
        '9': "f.h_28, f.h_29"
    }
    print("1")
    sqlstr = "SELECT h.name, " + str.get(keyId1) + "," + str.get(keyId2) + "," + str.get(keyId3) + " FROM hospitals h JOIN final_data f ON h.id = f.hospital_id"

    cursor = c.execute(sqlstr)

    row = cursor.fetchone()
    if row is None:
        print("找不到您要的資料訊息")
    while row is not None:
        print(row)
        row = cursor.fetchone()
    conn.close()
except:
   print("目前只能查詢八種特殊疾病")