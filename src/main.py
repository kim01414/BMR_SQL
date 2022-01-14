import tkinter as TK
import tkinter.ttk as TTK
import time
from tkcalendar import Calendar
from sub_windows import *

class MAIN_PROGRAM(TK.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1024x768+{0}+{1}'.format(self.winfo_screenwidth()//2-1024//2, self.winfo_screenheight()//2-768//2))
        self.title('BMR DB manager'); self.resizable(0,0)

        self.columns = ['번호','촬영일자','실험군','성명','차트번호', '촬영장소' ,'실험내용','촬영 시퀀스']; self.cols_size = [50,100,100,100,100,100,250,100]
        self.treeview = TTK.Treeview(self, columns=self.columns, displaycolumns=self.columns); self.treeview.place(x=10,y=10, width=900, height=750)
        for col, col_item in enumerate(self.columns):
            self.treeview.column('#{}'.format(col), width=self.cols_size[col])
            self.treeview.heading('#{}'.format(col), text=col_item)
        self.BTTN   = TK.Button(command=self.LOGIN,text='LOGIN'   )   ;  self.BTTN.place(x=920, y=10, width=94)
        self.BTTN2 = TK.Button(command=self.ADD_ROW,text='ADD',state='disabled');  self.BTTN2.place(x=920, y=40, width=94)
        self.BTTN3 = TK.Button(command=None ,text='EDIT'             ,state='disabled');  self.BTTN3.place(x=920, y=70, width=94)
        self.BTTN4 = TK.Button(command=None ,text='REMOVE'      ,state='disabled');  self.BTTN4.place(x=920, y=100, width=94)
        self.mainloop()

    def LOGIN(self):
       self.LOGIN_WIN = TK.Toplevel(self)
       self.LOGIN_WIN .geometry('320x160+{0}+{1}'.format(self.winfo_screenwidth()//2-160, self.winfo_screenheight()//2-80))
       self.LOGIN_WIN .title('Login'); self.LOGIN_WIN.resizable(0,0)
       image = TK.PhotoImage(file="../imgs/logo.png")
       label = TK.Label(self.LOGIN_WIN, image=image); label.image = image ; label.place(x=10,y=10)
       self.ID, self.PW = TK.StringVar(), TK.StringVar()
       self.LOGIN_WIN.grab_set()
       L1 = ttk.Label(self.LOGIN_WIN, text='Username:');L1.place(x=10, y=80)
       L2 = ttk.Label(self.LOGIN_WIN , text='Password:'); L2.place(x=10, y=120)
       E1 = ttk.Entry(self.LOGIN_WIN , textvariable=self.ID  );  E1.place(x=100, y=80)
       E2 = ttk.Entry(self.LOGIN_WIN , textvariable=self.PW, show='*'); E2.place(x=100, y=120)
       BTTN = TK.Button(self.LOGIN_WIN ,text='로그인', command=self.SERVER_LOGIN) 
       BTTN.place(x=260, y=90, width=50, height=40)
       
    def SERVER_LOGIN(self):
        DB = Network.LOGIN(self.ID.get(), self.PW.get())
        if DB is not None: 
            self.DB = DB; self.LOGIN_WIN.grab_release(); self.LOGIN_WIN.destroy(); self.REFRESH_TREE()
            self.BTTN.config(text='LOGOUT'); self.BTTN2.config(state='normal'); self.BTTN3.config(state='normal'); self.BTTN4.config(state='normal')
    
    def REFRESH_TREE(self):
        TABLE = Network.GET_TABLE(self.DB)
        try: self.treeview.delete(*self.treeview.get_children())
        except: pass
        for i, row in enumerate(TABLE):
            self.treeview.insert('','end',text=i, values=self.GET_ITEM(row), iid=str(i+1))

    def GET_ITEM(self,row):
        return [  row['촬영일자'].strftime('%Y-%m-%d'), row['실험군'], row['성명'], row['차트번호'], row['촬영장소'], row['실험내용'], row['촬영시퀀스']  ]

    def ADD_ROW(self):
        self.ADD_WIN = TK.Toplevel(self)
        self.ADD_WIN .geometry('550x220+{0}+{1}'.format(self.winfo_screenwidth()//2-225, self.winfo_screenheight()//2-110))
        self.ADD_WIN .title('환자정보 추가'); self.ADD_WIN.resizable(0,0)
        GET_TIME = time.localtime()
        self.cal = Calendar(self.ADD_WIN, selectmode = 'day', year = GET_TIME.tm_year, month = GET_TIME.tm_mon, day = GET_TIME.tm_mday); self.cal.place(x=10, y=10)
        for i,Item in enumerate(self.columns[2:]): ttk.Label(self.ADD_WIN,text=Item).place(x=270, y=25*(i+1))
        self.E1 =  TK.Entry(self.ADD_WIN); self.E1.place(x=350, y=25*(0+1), width=180)
        self.E2 = TK.Entry(self.ADD_WIN); self.E2.place(x=350, y=25*(1+1), width=180)
        self.E3 = TK.Entry(self.ADD_WIN); self.E3.place(x=350, y=25*(2+1), width=180)
        self.E4 = TK.Entry(self.ADD_WIN); self.E4.place(x=350, y=25*(3+1), width=180)
        self.E5 = TK.Entry(self.ADD_WIN); self.E5.place(x=350, y=25*(4+1), width=180)
        self.E6 = TK.Entry(self.ADD_WIN); self.E6.place(x=350, y=25*(5+1), width=180)
        ttk.Button(self.ADD_WIN,text='추가', command=self.ADD_ROW_CHILD).place(x=10, y=190, width=530)
    
    def ADD_ROW_CHILD(self, TABLE='환자정보'):
        AA = self.cal.get_displayed_month(); DATE ="%d-%02d-%02d"%(AA[1],AA[0], int(self.cal.get_date().split('.')[-2]))
        COMMIT = "INSERT INTO {0} VALUES ( '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}' )".format(TABLE, DATE, self.E1.get(), self.E2.get(), self.E3.get(), self.E4.get(), self.E5.get(), self.E6.get())
        Network.COMMIT_ORDER(self.DB, COMMIT)
        self.REFRESH_TREE()

        

if __name__ == '__main__':
    MAIN = MAIN_PROGRAM()
