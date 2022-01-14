import tkinter as TK
from tkinter import ttk
import Network

class LOGIN_WINDOW(TK.Toplevel):
    def __init__(self, parent):
        super().__init__(parent.WINDOW)
        self.Parent = parent
        self.grab_set()
        self.geometry('320x160+{0}+{1}'.format(self.winfo_screenwidth()//2-160, self.winfo_screenheight()//2-80))
        self.title('Login'); self.resizable(0,0)
        image = TK.PhotoImage(file="../imgs/logo.png"); label = TK.Label(self, image=image); label.place(x=10,y=10)
        self.ID, self.PW = TK.StringVar(), TK.StringVar()
        self.L1 = ttk.Label(self, text='Username:'); self.L1.place(x=10, y=80)
        self.L2 = ttk.Label(self, text='Password:'); self.L2.place(x=10, y=120)
        self.E1 = ttk.Entry(self, textvariable=self.ID  );  self.E1.place(x=100, y=80)
        self.E2 = ttk.Entry(self, textvariable=self.PW, show='*'); self.E2.place(x=100, y=120)
        self.BTTN = TK.Button(self, text='로그인', command=self.SERVER_LOGIN) 
        self.BTTN.place(x=260, y=90, width=50, height=40)
        self.protocol("WM_DELETE_WINDOW", quit)
        self.mainloop()
    
    def SERVER_LOGIN(self):
        DB = Network.LOGIN(self.ID.get(), self.PW.get())
        if DB is not None: 
            self.Parent.DB = DB
            self.grab_release()
            self.Parent.WINDOW.deiconify()
            self.destroy()
            