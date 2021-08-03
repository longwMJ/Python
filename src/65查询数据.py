import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 查询数据1
sql = "select * from Student"
values = cursor.execute(sql)
for i in values:
    print(i)

# 查询数据 2
sql = "select * from Student where id=?"
values = cursor.execute(sql, (1,))
for i in values:
    print('id:', i[0])
    print('name:', i[1])
    print('age:', i[2])

# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()