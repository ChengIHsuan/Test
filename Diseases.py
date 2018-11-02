import sqlite3
#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()

dis = str(input("特殊疾病"))
try:
    getId = c.execute("SELECT id FROM diseases WHERE (name LIKE '%" + dis + "%' OR eng_name LIKE '%" + dis + "%')")
    diseaseId = str(getId.fetchone()[0])
    str = {
        '1': "f.h_1, f.h_2, f.h_3, f.h_4, f.h_5",
        '2': "f.h_6, f.h_7, f.h_8, f.h_9, f.h_10, f.h_11",
        '3': "f.h_12, f.h_13, f.h_14, f.h_15",
        '4': "f.h_16, f.h_17, f.h_18",
        '5': "f.h_19, f.h_20, f.h_21, f.h_22",
        '6': "f.h_23, f.h_24, f.h_25, f.h_26, f.h_27",
        '7': "f.h_28, f.h_29, f.h_30, f.h_31",
        '8': "f.h_32, f.h_33" ##substr
    }
    sqlstr = "SELECT h.name, " + str.get(diseaseId) + " FROM hospitals h JOIN final_data f ON h.id = f.hospital_id"
    cursor = c.execute(sqlstr)

    row = cursor.fetchone()
    if row is None:
        print("找不到您要的資料訊息")
    while row is not None:
        print(row)
        row = cursor.fetchone()

    conn.close()
except:
    print("目前只有8個疾病相關的資訊，包括：氣喘疾病、急性心肌梗塞疾病、糖尿病、人工膝關節手術、腦中風、鼻竇炎、子宮肌瘤手術、消化性潰瘍疾病")