import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('test.db')

# 创建游标
cursor = conn.cursor()

cursor.execute("delete from Student where id=?",("1",)) #逗号不能省，元组元素只有一个的时候一定要加逗号,将删除lucy

# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()