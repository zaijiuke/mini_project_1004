import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title('Game')
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.user_name1 = tk.StringVar()
        self.user_name2 = tk.StringVar()
        self.size = tk.IntVar()

        self.get_user_names()
        self.get_board_size()

    def get_user_names(self):
        tk.Label(self.frame, text='Enter the first user name: ').grid(row=0, column=0)
        tk.Entry(self.frame, textvariable=self.user_name1).grid(row=0, column=1)
        tk.Label(self.frame, text='Enter the second user name: ').grid(row=1, column=0)
        tk.Entry(self.frame, textvariable=self.user_name2).grid(row=1, column=1)
        tk.Button(self.frame, text='Submit', command=self.check_names).grid(row=2, column=1)

    def check_names(self):
        if self.user_name1.get() != self.user_name2.get():
            self.frame.destroy()
        else:
            messagebox.showerror('Error', 'The players cannot use the same name. Please try again.')

    def get_board_size(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        tk.Label(self.frame, text='Choose your board size: 15 or 19: ').grid(row=0, column=0)
        tk.Entry(self.frame, textvariable=self.size).grid(row=0, column=1)
        tk.Button(self.frame, text='Submit', command=self.check_size).grid(row=1, column=1)

    def check_size(self):
        if self.size.get() in [15, 19]:
            self.frame.destroy()
            self.initialize_board()
        else:
            messagebox.showerror('Error', 'Wrong input, please try again.')

    def initialize_board(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        self.piece = [["+" for _ in range(self.size.get())] for _ in range(self.size.get())]
        for i in range(self.size.get()):
            for j in range(self.size.get()):
                tk.Button(self.frame, text=self.piece[i][j]).grid(row=i, column=j)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()