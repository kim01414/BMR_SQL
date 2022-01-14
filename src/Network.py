import pymysql as sql
import tkinter as TK
from tkinter import messagebox

def LOGIN(ID, PW, HOST='127.0.0.1'):
    try: 
        db = sql.connect(host=HOST, user=ID, passwd=PW, charset='utf8')
        print('Login successed!')
        return db
    except sql.err.OperationalError as E: 
        messagebox.showerror('오류!', E )
        return None
    except :
        messagebox.showerror('오류!', '알수 없는 에러.' )
        return None

def GET_TABLE(connection, DB='bmr_db', TABLE='환자정보'):
    curs = connection.cursor(sql.cursors.DictCursor)
    curs.execute('USE {}'.format(DB))
    curs.execute('select * from {}'.format(TABLE))
    return curs.fetchall()

def COMMIT_ORDER(connection, ORDER, DB='bmr_db', TABLE='환자정보'):
    print('UPLOAD {}'.format(ORDER))
    curs = connection.cursor(sql.cursors.DictCursor)
    curs.execute('USE {}'.format(DB))
    curs.execute(ORDER)
    connection.commit()