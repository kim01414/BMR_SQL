import tkinter as TK
from sub_windows import *

class MAIN_PROGRAM:
    def __init__(self):
        self.WINDOW = TK.Tk()
        self.WINDOW.geometry('1024x768+{0}+{1}'.format(self.WINDOW.winfo_screenwidth()//2-1024//2, self.WINDOW.winfo_screenheight()//2-768//2))
        self.WINDOW.title('BMR DB manager')
        self.WINDOW.withdraw()
        self.DB = None
        LOGIN_WINDOW(self)
        self.WINDOW.mainloop()

if __name__ == '__main__':
    MAIN = MAIN_PROGRAM()
