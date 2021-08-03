# 连接数据库 (如果不存在则创建)

import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')
print("Opened database successfully")

# 创建游标
cursor = conn.cursor()
# 关闭游标
cursor.close()
# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()