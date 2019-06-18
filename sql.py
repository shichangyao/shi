# !/usr/bin/python3
import pymysql
#连接数据库
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
print("Database version : %s " % data)
# 关闭数据库连接
db.close()
#数据库建表
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 使用预处理语句创建表
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""
cursor.execute(sql)
# 关闭数据库连接
db.close()
#数据库插入操作
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()
# 关闭数据库连接
db.close()
#另一种方法
# !/usr/bin/python3
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
      ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
#以下代码使用变量向SQL语句中传递参数：
user_id = "root"
password = "YAOrui0626."
con.execute('insert into Login values( %s,  %s)' % \
             (user_id, password))
#数据库查询操作
#Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
# fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# fetchall(): 接收全部的返回结果行.
# rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
import pymysql
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE \
       WHERE INCOME > %s" % (1000)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % \
              (fname, lname, age, sex, income))
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
#数据库更新操作
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()
#删除操作
# SQL 删除语句
# 打开数据库连接
db = pymysql.connect("localhost", "root", "YAOrui0626.", "mysql")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 提交修改
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭连接
db.close()