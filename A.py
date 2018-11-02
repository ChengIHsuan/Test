import sqlite3
#connect
conn = sqlite3.connect('voyager.db')
c = conn.cursor()
###
class Search():
    def regionSearch(county, township):
        i = county.find("北")
        if i != -1:
            area = str("_北%" + township)
        else:
            area = str(county + '%' + township)

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

    def diseaseSearch(disease):
        print(disease)
        try:
            getId = c.execute("SELECT id FROM diseases WHERE name LIKE '%" + str(disease) + "%'")
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
        except:
            print("目前只能查詢八種特殊疾病")

    diseaseSearch("氣喘")
    conn.close()
