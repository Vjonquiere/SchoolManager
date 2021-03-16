from tkinter import *
import sqlite3
from PIL import ImageTk 

class GUI:
    def __init__(self, master, id,sql_db):
        
        #### Window options
        self.m = master
        self.m.minsize(900,250)
        
       
        #### Seting up frames | credits : https://pythonbasics.org/tkinter-frame/
        self.absence_frame = Frame(self.m,highlightbackground="black",highlightthickness=1)
        self.absence_frame.grid(column=1,row=0,padx = 10)
        
        self.grade_frame = Frame(self.m,highlightbackground="red",highlightthickness=1)
        self.grade_frame.grid(column=0,row=0,sticky=N)
        
        #### SQL import
        self.id = id
        self.sql = sql_db
        

        #### Basic Datas
        self.m.title("Eleve: " + self.sql.get_firstname() + " " + self.sql.get_name()  + " " + self.sql.get_classroom())
        self.images_displayed = {}
        self.absence_label = Label(self.absence_frame, text="Recent absences: ").grid(column=0, row=0, sticky = E)
        self.absence_label = Label(self.grade_frame, text="Recent grades: ").grid(column=0, row=0, sticky = NE)
        self.display_abenses()
        self.display_grade()
        print(self.sql.get_grades())
    
        
    def display_abenses(self):
        
        absence = self.sql.get_student_absences()
        
        if len(absence) == 0:
            self.no_absence_label = Label(self.absence_frame, text="Nothing recent here").grid(row=0,column=1)
            
        for i in range(len(absence)):
            self.show = Label(self.absence_frame,text="debut: " + str(absence[i][0]) + "    |    fin: " + str(absence[i][1]))
            self.show.grid(row = i, column = 1)
            if absence[i][2] == "True":
                self.display_image(2 ,i ,"icons/icon_checked.png")
            else:
                self.display_image(2 ,i ,"icons/icon_cancel.png")
       
         
    def display_image(self, x, y, img):
        self.img = ImageTk.PhotoImage(master = self.absence_frame,file=img)
        self.images_displayed["row{0}".format(y)] = Label(self.absence_frame, image=self.img)
        self.images_displayed["row{0}".format(y)].image = self.img
        self.images_displayed["row{0}".format(y)].grid(column=x ,row=y)
      
    def display_grade(self):
        
        grades = self.sql.get_grades()
        
        if len(grades) == 0:
            self.no_grade_label = Label(self.grade_frame,text='Nothing recent here').grid(row=0,column=1)
        for i in range(len(grades)):
            self.show = Label(self.grade_frame,text = str(grades[i][0]) + " " +str(grades[i][1]) + "/" + str(grades[i][2]) + "\nfait le: " + grades[i][3])
            self.show.grid(row = i, column = 1,sticky=SE) 

        
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
        self.c.execute('''SELECT debut,fin,justification_valide FROM absence WHERE eleve_id = ?  ''', self.data)
        return self.c.fetchall()

    def get_grades(self):
        self.data = (self.id_eleve,)
        self.c.execute('''SELECT matiere,note,note_max,date FROM note WHERE eleve_id = ?''',self.data)
        return self.c.fetchall()
        
    
    
def test(id):
    s = SQL(id)
    root = Tk()
    my_gui = GUI(root, id, s)
    root.mainloop()
