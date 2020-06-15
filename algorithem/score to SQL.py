import pymysql
import json
dict_temp = dict()

db = pymysql.connect(host='localhost', port=3306, user='root', password='123456', db='hashtag_demo')
cursor = db.cursor()
with open('E:/hashtag_clean_data/hashtag_count2.txt', 'r',encoding="utf-8") as f:
    json = f.readlines()
    for line in json:
        line = line.strip()
        k = line.split(' ')[0]
        v = line.split(' ')[1]
        dict_temp[k] = v
    print(dict_temp)
for key, value in dict_temp.items():
    hashtag = key
    amount = value
    sql = "insert into `hashtag_count` (`hashtag`, `count`) values ('" + key + "', " + amount + ")"
    try:
        cursor.execute(sql)
    except Exception as e:
        print("Error", str(e), sql)
        pass
db.commit()
db.rollback()
cursor.close()







