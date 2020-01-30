import pymysql


def sql_insert(idx,stock_code):
    db = pymysql.connect(host='localhost',
                         user='host',
                         password='1234',
                         db='project',
                         charset='utf8')
    try:
        cursor =db.cursor()
        sql='insert into favorite(idx,stock_code,fav) values('+idx+','+stock_code+',1)'
        cursor.execute(sql)
        db.commit()
    finally:
        db.close()

def sql_select_all(table):
    db = pymysql.connect(host='localhost',
                         user='host',
                         password='1234',
                         db='project',
                         charset='utf8')

    try:
        with db.cursor() as cursor:
            sql = "select * from "+table
            cursor.execute(sql)
            result = cursor.fetchall()
            temp = []
            for row_data in result:
                temp.append(row_data)
            return temp;

    finally:
        db.close()

def sql_select1(table,idx):
    db = pymysql.connect(host='localhost',
                         user='host',
                         password='1234',
                         db='project',
                         charset='utf8')

    try:
        with db.cursor() as cursor:
            sql = "select * from "+table+" where idx="+idx
            cursor.execute(sql)
            result = cursor.fetchall()
            temp=[]
            for row_data in result:
                temp.append(row_data)
            return temp;
    finally:
        db.close()

def sql_select2(table,idx,stock_code):
    db = pymysql.connect(host='localhost',
                         user='host',
                         password='1234',
                         db='project',
                         charset='utf8')

    try:
        with db.cursor() as cursor:
            sql = "select * from "+table+" where idx="+idx+" and "+"stock_code="+stock_code
            cursor.execute(sql)
            result = cursor.fetchall()
            temp=[]
            for row_data in result:
                temp.append(row_data)
            return temp;
    finally:
        db.close()


def sql_delete(idx,stock_code):
    db = pymysql.connect(host='localhost',
                         user='host',
                         password='1234',
                         db='project',
                         charset='utf8')
    try:
        cursor = db.cursor()
        sql = 'delete from favorite where idx='+ idx + ' and stock_code='+ stock_code
        cursor.execute(sql)
        db.commit()
    finally:
        db.close()
