from tkinter import *
from PIL import Image, ImageTk
import os
import socket
from tkinter import messagebox
from tkinter import ttk

class Socket():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = 'localhost'
        if self.connect():
            print('Connected')
        else:
            print('no')
            messagebox.showerror('Connection', 'Failed to connect, Try again')


    def connect(self):
        try:
            self.sock.connect((self.ip, 8888))
            return True
        except ConnectionRefusedError:
            return False

    def Login(self, user):
        self.sock.send('login'.encode())
        self.sock.send('Samuel_Scott@544464'.encode())




    def Refresh(self):
        self.sock.send('refresh'.encode())
        self.sock.send('Samuel_Scott@544464'.encode())
        self.sock.recv(1024).decode()


class Main:
    def __init__(self):
        self.loc = os.path.dirname(os.path.relpath(__file__))
        self.root = Tk()
        self.root.title('')
        self.root.geometry('600x500')
        self.root.resizable(0, 0)
        self.ver = 'V.0.1'
        self.root.config(bg='white')
        self.login = Button(self.root, text='Login', command=lambda: self.Login())
        self.refresh = Button(self.root, text='Refresh', command=lambda: Socket().Refresh())
        self.refresh.pack()
        self.Login()

    def Login(self):
        # init
        self.login = Button(self.root, text='Login', command=lambda: self.Login())

        OptionList = [
            "Click your name",
            "Samuel Scott"
        ]
        print(OptionList)

        variable = StringVar(self.root)
        variable.set(OptionList[0])

        opt = ttk.OptionMenu(self.root, variable, *OptionList)
        self.login.place(x=250, y=400)
        opt.place(x=100, y=150, width=200)






MainMF = Main()
MainMF.root.mainloop()
