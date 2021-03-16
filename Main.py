from tkinter import *

import sqlite3, sys, hashlib
from SchoolManager import professor_panel, eleve_panel, school_office



class GUI:
    
    def __init__(self, master):
        self.master = master
        self.master.minsize(300,175)
        self.master.maxsize(300,175)
        self.master.title("School Manager Login")
        
        self.font = "fonts/Nunito"
        
        
        self.error  = False
        
        self.master.columnconfigure(1,pad = 10,minsize= 50)
        ##### Connexion DB ####
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        
        ##### Structure label ####
        self.title = Label(text = "Login Page", font=("Impact",15)).grid(column=3, row=0, pady = (0,10))
        self.login_label = Label(text = "Login", font = (self.font, 10)).grid(column=2,row=1,sticky = E, pady=(0,5))
        self.login_label = Label(text = "Password",font = (self.font, 10)).grid(column=2,row=2,sticky = E, pady=(0,5))
        
        ##### Structure champs####
        self.login = StringVar()
        self.login_champs = Entry(textvariable = self.login, width = 10)
        self.login_champs.grid(column = 3, row = 1)
        
        self.mdp = StringVar()
        self.mdp_champs = Entry(textvariable = self.mdp, show="*", width = 10)
        self.mdp_champs.grid(column = 3, row = 2)
        
        #### button ####
        
        self.log_button = Button(self.master,command = self.login_test, text= "login", font = (self.font,10), width = 4, height = 1).grid(column=3,row=3, pady = (5,0))
    
    def login_test(self):
        
        # dev connexion
        #self.mdpde = mdp
        #self.hash_mdp = hashlib.md5(self.mdpde.encode()).hexdigest()
        #self.data = (identifiant,self.hash_mdp)
        

        self.hash_mdp = hashlib.md5(self.mdp_champs.get().encode()).hexdigest()
        self.data = (self.login_champs.get(),self.hash_mdp)
        
        self.c.execute('''SELECT * FROM users WHERE login = ? AND mdp = ?''', self.data)
        self.a = self.c.fetchall()

            
        if len(self.a) == 0:
            self.error_message("login/passwd \n invalid")
            if len(self.login_champs.get()) == 0 or len(self.mdp_champs.get()) == 0:
                self.error_message("need login \n and passwd")
        else:
            self.return_data = self.a[0]
            if self.return_data[3] == "eleve":
                eleve_panel.launch(self.return_data[0])
            if self.return_data[3] == "school_office":
                school_office.launch(self.return_data[0])
            if self.return_data[3] == "professor":
                professor_panel.launch(self.return_data[0])
                
        
    def error_message(self, error):
        if self.error :
            self.error_mes.grid_remove()
        
        self.error_mes = Label(self.master,text = error,font = ("Nunito", 10))
        self.error_mes.grid(row=4,column=3)
        self.error = True
        
        
root = Tk()
my_gui = GUI(root)
root.mainloop()
