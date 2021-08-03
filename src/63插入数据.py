import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

# 插入数据1
sql = "INSERT INTO Student(Name, Age) VALUES(\'lucy\', 22)"
cursor.execute(sql)

# 插入数据 2
data = ('jack', 21) 
sql = "INSERT INTO Student(Name, Age) VALUES(?, ?)"
cursor.execute(sql, data)

# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()