# import sqlite3



# conn = sqlite3.connect('novel.db')

# sql = 'select * from novel'

# cur = conn.cursor()

# cur.execute(sql)

# print(cur.fetchall())

# cur.close()
# conn.close()


# 连接数据库 (如果不存在则创建)

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('novel.db')
print("Opened database successfully")

# 创建游标
cursor = conn.cursor()
# # 关闭游标
# cursor.close()

# 创建表
sql = 'CREATE TABLE Novel(id integer PRIMARY KEY autoincrement, Name  varchar(30), Age integer)'
cursor.execute(sql)

# 插入数据1
sql = "INSERT INTO Novel(Name, Age) VALUES(\'lucy\', 22)"
cursor.execute(sql)

# 插入数据 2
data = ('jack', 21) 
sql = "INSERT INTO Novel(Name, Age) VALUES(?, ?)"
cursor.execute(sql, data)
cursor.execute(sql, ('龙', 33))

# 查询数据1
sql = "select * from Novel"
values = cursor.execute(sql)
for i in values:
    print(i)

# 查询数据 2
sql = "select * from Novel where id=?"
values = cursor.execute(sql, (1,))
for i in values:
    print('id:', i[0])
    print('name:', i[1])
    print('age:', i[2])

#删除表格Student
cursor.execute("DROP TABLE Novel")


# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()

