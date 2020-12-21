from tkinter import *
import sqlite3


class GUI:
    def __init__(self, master, id):
        
        self.m = master
        self.m.minsize(300,250)
        self.m.maxsize(300,250)
        
        self.id = id
        self.m.title("session n°" + str(self.id))
        
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        self.title = Label(self.m,text="School Manager : Student").grid(column=1,row=1)
        
        self.get_basic_infos()
        
    
    def get_basic_infos(self):
        
        self.data = (self.id,)
        self.c.execute('''SELECT nom,prenom,classe,nbr_absence FROM eleve WHERE id = ? ''', self.data)
        self.a = self.c.fetchall()

        self.nom = self.a[0][0]
        self.prenom = self.a[0][1]
        self.classe = self.a[0][2]
        
        self.m.title("Elève: " + str(self.prenom) + " " + str(self.nom) + " " + str(self.classe))

        
    
def test(id):
    root = Tk()
    my_gui = GUI(root, id)
    root.mainloop()
    