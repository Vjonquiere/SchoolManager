from tkinter import *
import sqlite3,hashlib

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.minsize(300,250)
        self.master.maxsize(300,250)
        
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        #### CREATION DES TABLES NECESSAIRES ####
        self.c.execute('''CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, mdp TEXT, role TEXT);''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS eleve(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, niveau INT, classe TEXT, nbr_absence INT, dp BOOLEAN );''')
        
        self.menu()
        
    def menu(self):
        while True:
            self.nom = input("nom: ")
            self.prenom = input("prenom: ")
            self.niveau = input("niveau: ")
            self.classe = input("classe: ")
            self.nbr_absence = 0
            self.dp = input("demi-pensionnaire : ")
            
            self.data_person = (self.nom,self.prenom,self.niveau,self.classe,self.nbr_absence,self.dp)
            
            self.c.execute('''INSERT INTO eleve VALUES (NULL,?,?,?,?,?,?)''',self.data_person)
            self.connexion.commit()
            
            self.hash_mdp = hashlib.md5(self.nom.encode()).hexdigest()
            self.data_login = (self.prenom, self.hash_mdp,)
            self.c.execute('''INSERT INTO person VALUES (NULL,?,?,"eleve")''',self.data_login)
            self.connexion.commit()
            
root = Tk()
my_gui = GUI(root)
root.mainloop()