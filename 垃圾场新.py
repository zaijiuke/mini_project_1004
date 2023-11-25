import tkinter as tk
from tkinter import messagebox
import sys
class Game:
    def __init__(self,LOL):
        self.LOL=LOL
        self.LOL.title('wuziqi')
        self.LOL.geometry('500x500')
        self.frame1=tk.Frame(self.LOL)
        self.frame1.pack()

        self.user_name1=tk.StringVar()
        self.user_name2=tk.StringVar()
        self.board_size=tk.StringVar()

        self.get_user_name()

    def packin_frame2(self):
        self.frame2=tk.Frame(self.LOL)
        self.frame2.pack()

    def show_chess(self):
        tk.Label(self.frame2,text=self.user_name1.get()+', you will use black').grid(row=0)
        tk.Label(self.frame2,text=self.user_name2.get()+', you will use wight').grid(row=1)
        tk.Button(self.frame2,text='confirm',command=self.delete_frame2).grid(row=2)


    def get_user_name(self):
        tk.Label(self.frame1,text='enter the first user name: ').grid(row=0,column=0)
        tk.Entry(self.frame1,textvariable=self.user_name1).grid(row=0,column=1)
        tk.Label(self.frame1,text='enter the second user name: ').grid(row=1,column=0)
        tk.Entry(self.frame1,textvariable=self.user_name2).grid(row=1,column=1)
        tk.Label(self.frame1,text='choose the size of board, 15 or 19').grid(row=2,column=0)
        tk.Entry(self.frame1,textvariable=self.board_size).grid(row=2,column=1)
        tk.Button(self.frame1,text='confirm',command=self.judge_name_size).grid(row=3,column=1)
    
    def judge_name_size(self):
        if self.user_name1.get() != self.user_name2.get() and (self.board_size.get()=='15' or self.board_size.get()=='19'):
            self.frame1.destroy()
            self.packin_frame2()
            self.show_chess()
            global size
            size=self.board_size.get()
            size=int(size)
        elif self.user_name1.get() == self.user_name2.get() and (self.board_size.get()=='15' or self.board_size.get()=='19'):
            messagebox.showerror('Warning','The names of users cannot be the same. Please try again.')
        elif self.user_name1.get() != self.user_name2.get() and (self.board_size.get()!='15' or self.board_size.get()!='19'):
            messagebox.showerror('Warning','The size of board should be 15 or 19. Please try again.')
        else:
            messagebox.showerror('Warning','Wrong enter. Please try again.')

    def delete_frame2(self):
        self.frame2.destroy()
        self.packin_frame3()

    def packin_frame3(self):
        self.frame3=tk.Frame(self.LOL)
        self.frame3.pack()
        self.make_board()

    def make_board(self):
        piece=[["+"for i in range(size)] for j in range(size)]
        tool1=[]
        tool2=[]
        for x in range(10):
            tool1.append('0')
        for y in range(size-10):
            tool1.append('1')
        for z in range(10):
            tool2.append(str(z))
        for oi in range(size-10):
            tool2.append(str(oi))
        piece.append(tool1)
        piece.append(tool2)
        for pq in range(size):
            piece[pq].append(str(pq))
        for row in piece:
            piece_new=' '.join(row)
        tk.Label(self.frame3,text=piece_new).grid(row=0)
        tk.Button(self.frame3,text='confirm',command=self.delete_frame3).grid(row=1)
        
    def delete_frame3(self):
        self.frame3.destroy()




    # def wuziqihudong(self):
        

    # def whatcolor1(name):
    #     a.append(name)
    #     lb.config(text=f'{name},you will use black stones',fg='black')
        
    # def whatcolor2(name):
    #     lb.config(text=f'{name},you will use white stones',fg='black')
    #     b.append(name)
    # def change_user():
    #     lb.config(text='enter the second user name',height=1,width=50,fg='black')
    # text = tk.Entry(app,width=10)
    # text.pack()
    # b1=tk.Button(text='confirm',width=10,bg='white',command=lambda:whatcolor1(text.get()))
    # b1.pack()

app = tk.Tk()
game=Game(app)
tk.mainloop()