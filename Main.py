from tkinter import *
import sqlite3, sys, hashlib

class GUI:
    
    def __init__(self, master):
        self.master = master
        self.master.minsize(300,250)
        self.master.maxsize(300,250)
        
        self.master.columnconfigure(1,pad = 10,minsize= 50)
        ##### Connexion DB ####
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        self.c.execute('''CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, mdp TEXT, role TEXT);''')
        
        ##### Structure label ####
        self.title = Label(text = "Login Page").grid(column=3, row=0)
        self.login_label = Label(text = "Login").grid(column=2,row=1,sticky = E)
        self.login_label = Label(text = "Password").grid(column=2,row=2,sticky = E)
        
        ##### Structure champs####
        self.login = StringVar()
        self.login_champs = Entry(textvariable = self.login, width = 8)
        self.login_champs.grid(column = 3, row = 1)
        
        self.mdp = StringVar()
        self.mdp_champs = Entry(textvariable = self.mdp, show="*", width = 8)
        self.mdp_champs.grid(column = 3, row = 2)
        
        #### button ####
        
        self.log_button = Button(self.master,command = self.log_test, text= "login").grid(column=3,row=3)
        
    def log_test(self):
        self.hash_mdp = hashlib.md5(self.mdp_champs.get().encode()) 
        
        
        
root = Tk()
my_gui = GUI(root)
root.mainloop()