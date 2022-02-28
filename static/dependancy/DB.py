
import psycopg2

#DBコネクト関数
def connect(HOST,PORT,DBNAME,USER,PASSWORD):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa ', HOST,PORT,DBNAME,USER,PASSWORD)
    con = psycopg2.connect("host=" + HOST + " port=" + PORT + " dbname=" + DBNAME + " user=" + USER + " password=" + PASSWORD)
    return con

def lock(CON, SQL):
    with CON.cursor() as cur:
        cur.execute(SQL)

#検索関数
def select_execute(CON, SQL):
    with CON.cursor() as cur:
        cur.execute(SQL)
        rows = cur.fetchall()
    return rows

def select_execute2(CON, SQL):
    with CON.cursor() as cur:
        cur.execute(SQL)

#登録関数
def insert_execute(CON, SQL, SQL1):
    #insert実行
    with CON.cursor() as cur:
        cur.execute(SQL1)
    #結果取得
    res = select_execute(CON,SQL)
    CON.commit()
    return res

#削除関数
def delete_execute(CON, SQL, SQL1):
    with CON.cursor() as cur:
        cur.execute(SQL1)
    #検索実行
    res = select_execute(CON,SQL)
    CON.commit()
    return res

#更新関数
def update_execute(CON, SQL, SQL1):
    with CON.cursor() as cur:
        cur.execute(SQL1)
    #検索実行
    res = select_execute(CON,SQL)
    CON.commit()
    return res

#特定ラベル項目検索関数
def select_item_execute(CON, SQL1):
    with CON.cursor() as cur:
        cur.execute(SQL1)
        rows = cur.fetchall()
    CON.commit()
    return rows


"""
# DB接続情報 
DB_HOST = 'svl14065-vm01'
DB_PORT = '5432'
DB_NAME = 'SAITAMA_LABEL'
DB_USER = 'postgres'
DB_PASS = 'postgres_365'
"""