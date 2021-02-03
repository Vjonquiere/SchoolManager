from tkinter import *
import sqlite3
from PIL import ImageTk 

class GUI:
    def __init__(self, master, id,sql_db):
        
        self.m = master
        self.m.minsize(500,250)
       
        
        self.id = id
        self.sql = sql_db
        self.images_displayed = {}
        
        #self.img = ImageTk.PhotoImage(master = self.m,file="icons/rsz_icons8-cancel-48.png")
        #self.images_displayed["nike"] = Label(self.m, image=self.img)
        #self.images_displayed["nike"].grid(row=10,column=4)
        
        
        self.display_image( 3, 7)
        
        self.m.title("Eleve: " + self.sql.get_firstname() + " " + self.sql.get_name()  + " " + self.sql.get_classroom())
        
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        self.title = Label(self.m,text="School Manager : Student").grid(column=1,row=0)
        

        #### Basic Labels
        
        self.absence_label = Label(self.m, text="Absence: ").grid(column=1, row=1, sticky = E)
        
        
        self.display_abenses()
        
    
        
    def display_abenses(self):
        
        absence = self.sql.get_student_absences()
        
        for i in range(len(absence)):
            self.show = Label(self.m,text="debut: " + str(absence[i][0]) + "    |    fin: " + str(absence[i][1]))
            self.show.grid(row = 1 + i, column = 2)
            
            
    def display_image(self, x, y):
        
        self.img = ImageTk.PhotoImage(master = self.m,file="icons/rsz_icons8-cancel-48.png")
        self.images_displayed["row{0}".format(y)] = Label(self.m, image=self.img)
        self.images_displayed["row{0}".format(y)].grid(column=x ,row=y)
        print(self.images_displayed)

class SQL:
    
    def __init__(self, id_eleve):
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        self.id_eleve = id_eleve
        
        
    def get_name(self):
        self.data = (self.id_eleve,)
        self.c.execute('''SELECT nom FROM eleve WHERE id_eleve = ? ''', self.data)
        return self.c.fetchall()[0][0]
    
    def get_firstname(self):
        self.data = (self.id_eleve,)
        self.c.execute('''SELECT prenom FROM eleve WHERE id_eleve = ? ''', self.data)
        return self.c.fetchall()[0][0]
    
    def get_classroom(self):
        self.data = (self.id_eleve,)
        self.c.execute('''SELECT classe FROM eleve WHERE id_eleve = ? ''', self.data)
        return self.c.fetchall()[0][0]     
       
    def get_student_absences(self):
        self.data = (self.id_eleve,)
        self.c.execute('''SELECT debut,fin FROM absence WHERE eleve_id = ?  ''', self.data)
        return self.c.fetchall()



        
def test(id):
    s = SQL(1)
    root = Tk()
    my_gui = GUI(root, id, s)
    print(type(my_gui))
    print(my_gui.title)
    root.mainloop()
    