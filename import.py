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


f = open("I:\\pangqian\\roadLink\\zhangxingtong.csv")  # 返回一个文件对象
line = f.readline()  # 调用文件的 readline()方法
line = f.readline()
while line:

    content = line.split(",")
    params = (content[0], content[1], content[2], content[3], content[4])

    sql = "INSERT INTO hway_zhangxingtong (station_id, station_name, province, longi, lati) VALUES(?,?,?,?,?)"

    c.execute(sql, params)
    line = f.readline()

f.close()

print("Import successfully")

conn.commit()
conn.close()
