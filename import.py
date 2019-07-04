#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('db.sqlite3')
print("I:\\故障路段数据\\Opened database successfully")
c = conn.cursor()

# c.execute('''CREATE TABLE hway_chongqing_od
#        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
#        link_id INT  NOT NULL,
#        enstation VARCHAR(10) NOT NULL,
#        exstation VARCHAR(10) NOT NULL,
#        txl INT  NOT NULL,
#        province_id INT  NOT NULL,
#        province VARCHAR(10) NOT NULL);''')

# f = open("I:\\pangqian\\roadLink\linkToOD\\guizhou.csv", 'r', encoding='UTF-8')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
#
# while line:
#     sql = "INSERT INTO hway_linktood (link_id, enstation, exstation, txl, number, province) VALUES \n "
#
#     tmp = line.split(":")
#     content = tmp[1].split(";")
#
#     for subStr in content:
#         toll = subStr.split(",")
#
#         sql += "(" + tmp[0] + ", '" + toll[0] + "', '" + toll[1] + "', '" + toll[2] + "', '" + toll[3] + "', '" + toll[
#             4] + "'),"
#
#     sql = sql[:-1] + "; \n"
#     c.execute(sql)
#     line = f.readline()
#
# f.close()

#
# f = open("I:\\pangqian\\roadLink\\zhangxingtong.csv")  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
# line = f.readline()
# while line:
#
#     content = line.split(",")
#     params = (content[0], content[1], content[2], content[3], content[4])
#
#     sql = "INSERT INTO hway_zhangxingtong (station_id, station_name, province, longi, lati) VALUES(?,?,?,?,?)"
#
#     c.execute(sql, params)
#     line = f.readline()
#
# f.close()

f = open("I:\\programData\\chongqingCoeCal\\travelCoePerYear01\\16-19出行系数结果.csv", 'r', encoding='UTF-8')  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
line = f.readline()

while line:
    sql = "INSERT INTO hway_travelcoe (enSta_id, exSta_id, date, vehType, txl, travelCoe) VALUES \n "

    content = line.split(",")
    line = f.readline()
    if(int(content[4]) >= 60 or int(content[4]) < 20):
        continue

    sql += "(" + content[0] + ", '" + content[1] + "', '" + content[2] + "', '" + content[3] + "', '" + content[4] + "', '" + content[
        7] + "'),"

    sql = sql[:-1] + "; \n"
    c.execute(sql)

f.close()

# f = open("H:\\G_1149\\系数计算文件\\station.csv", 'r', encoding='gbk')  # 返回一个文件对象
# line = f.readline()  # 调用文件的 readline()方法
#
# while line:
#     sql = "INSERT INTO hway_cqodlocation(station_id, longi, lati) VALUES \n "
#
#     content = line.split(",")
#     line = f.readline()
#
#     sql += "(" + content[2] + ", '" + content[0] + "', '" + content[1] + "'),"
#
#     sql = sql[:-1] + "; \n"
#     c.execute(sql)
#
# f.close()

print("Import successfully")

conn.commit()
conn.close()
