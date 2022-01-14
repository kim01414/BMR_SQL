import tkinter as TK
import tkinter.ttk as TTK
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

        self.BTTN = TK.Button(command=self.LOGIN,text='LOGIN')
        self.BTTN.place(x=920, y=10, width=94)
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
            self.DB = DB
            self.LOGIN_WIN.grab_release()
            self.LOGIN_WIN.destroy()
            TABLE = Network.GET_TABLE(self.DB)
            for i, row in enumerate(TABLE):
                self.treeview.insert('','end',text=i, values=self.GET_ITEM(row), iid=str(i+1))

    def GET_ITEM(self,row):
        return [ 
            row['촬영일자'].strftime('%Y-%m-%d'), row['실험군'], row['성명'], row['차트번호'], row['촬영장소'], row['실험내용'], row['촬영시퀀스']
        ]

if __name__ == '__main__':
    MAIN = MAIN_PROGRAM()
