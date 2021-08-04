
import sqlite3

# 连接数据库(如果不存在则创建)
conn = sqlite3.connect('novel.db')
print("Opened database successfully")

# 创建游标
cursor = conn.cursor()
# # 关闭游标
# cursor.close()

# CREATE TABLE "novel" (
# 	"id"	INTEGER NOT NULL UNIQUE,
# 	"Name"	TEXT,
# 	"Title"	TEXT,
# 	"Content"	INTEGER,
# 	PRIMARY KEY("id" AUTOINCREMENT)
# )

# 创建表
# sql = 'CREATE TABLE NovelDemoTextABCDEFAABC(id integer PRIMARY KEY autoincrement, Name  varchar(30), Age integer)'
sql = 'CREATE TABLE NovelDemoTextABCDEFAABC(id integer PRIMARY KEY autoincrement, Name  TEXT, title TEXT, content TEXT)'
cursor.execute(sql)

# 插入数据1
sql = "INSERT INTO NovelDemoTextABCDEFAABC(Name, Title, Content) VALUES(\'lucy\', \'Titlelucy\', \'Contentlucy\')"
cursor.execute(sql)

# 插入数据 2
data = ('jack', 'jack12', 'jack23') 
# sql = "INSERT INTO NovelDemoTextABCDEFAABC(Name, Title, Content) VALUES(?, ?, ?)"

sql = "INSERT INTO NovelDemoTextABCDEFAABC(Name, Title, Content) VALUES(?, ?, ?)"
cursor.execute(sql, data)
cursor.execute(sql, ('jack', 'jack56', 'jack78') )
cursor.execute(sql, ('56', '', '') )


# # ???
# sql = "UPDATE NovelDemoTextABCDEFAABC(Title, Content) VALUES(\'lucy\', \'lucy\') where Name=\'56\'"
# UPDATE Person SET Address = 'Zhongshan 23', City = 'Nanjing' WHERE LastName = 'Wilson';

# good
# sql = "UPDATE NovelDemoTextABCDEFAABC SET Title = \'lucyuuuu\' WHERE Name=\'56\'"
# sql = "UPDATE NovelDemoTextABCDEFAABC SET(Title, Content) VALUES(\'lucyHHHHY\', \'lucy\') WHERE Name=\'56\'"
# good
# sql = "UPDATE NovelDemoTextABCDEFAABC SET Title = ? WHERE Name=\'56\'"
sql = "UPDATE NovelDemoTextABCDEFAABC SET Title = ?, Content = ? WHERE Name=?"

# cursor.execute(sql, ('即佛鳄我', '有条件'), ('56',) )
# good
# cursor.execute(sql) 
cursor.execute(sql, ('即佛鳄我214', '合肥u为荣华富贵', '56') )

# 查询数据1
sql = "select * from NovelDemoTextABCDEFAABC"
values = cursor.execute(sql)
for i in values:
    print(i)

# 查询数据 2
sql = "select * from NovelDemoTextABCDEFAABC where id=?"
values = cursor.execute(sql, (4,))
for i in values:
    print('id:', i[0])
    print('Name:', i[1])
    print('Title:', i[2])
    print('Content:', i[3])

#删除表格Student
cursor.execute("DROP TABLE NovelDemoTextABCDEFAABC")


# 提交事物
conn.commit()

#关闭游标
cursor.close()

#关闭连接
conn.close()

