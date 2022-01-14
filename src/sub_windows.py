from cgitb import text
import tkinter as TK
from tkinter import ttk

class LOGIN_WINDOW:
    def __init__(self, parent):
        self.WINDOW = TK.Toplevel()
        self.WINDOW.geometry('320x160+{0}+{1}'.format(self.WINDOW.winfo_screenwidth()//2-160, self.WINDOW.winfo_screenheight()//2-80))
        self.WINDOW.title('Login'); self.WINDOW.resizable(0,0)

        image = TK.PhotoImage(file="../imgs/logo.png"); label = TK.Label(self.WINDOW, image=image); label.place(x=10,y=10)
        self.ID, self.PW = TK.StringVar(), TK.StringVar()

        self.L1 = ttk.Label(self.WINDOW, text='Username:'); self.L1.place(x=10, y=80)
        self.L2 = ttk.Label(self.WINDOW, text='Password:'); self.L2.place(x=10, y=120)
        self.E1 = ttk.Entry(self.WINDOW, textvariable=self.ID  );  self.E1.place(x=100, y=80)
        self.E2 = ttk.Entry(self.WINDOW, textvariable=self.PW, show='*'); self.E2.place(x=100, y=120)
       
        self.BTTN = TK.Button(self.WINDOW, text='로그인', command=None)
        self.BTTN.place(x=260, y=90, width=50, height=40)
        

        self.WINDOW.mainloop()