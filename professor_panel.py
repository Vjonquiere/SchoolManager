from tkinter import *
import sqlite3
import time
import datetime

class GUI:
    
    def __init__(self,master, sql):
        self.master = master
        self.master.title("Professor Panel")
        self.master.minsize(500,500)
        
        self.add_grade = Frame(self.master)
        self.add_grade.grid(column=0,row=0)
        
        self.signal_absence = Frame(self.master)
        self.signal_absence.grid(column=0,row=1)
        
        self.make_absence_alert = Frame(self.master)
        self.make_absence_alert.grid(column=0,row=1)
        
        self.sql = sql
        
        self.need_clear = False
        
    ###### setup basic widget
    
        self.add_grade_title = Label(self.add_grade, text="Add a grade: ").grid(column=0,row=0)
        
        self.grade_classroom = StringVar()
        self.add_grade_classroom_entry = Entry(self.add_grade, textvariable=self.grade_classroom, width = 6)
        self.add_grade_classroom_entry.grid(column=1,row=0)
        
        self.search_classroom_button = Button(self.add_grade, text="Search", command = self.setup_grade_environment).grid(column=2,row=0)
        
        self.submit_button = Button(self.add_grade, command = self.verify_inputed_data, text="submit").grid(column=10,row=0)
        
        
       
       
################################################################################################################################################################################      
################################################################################## GRADE PART ##################################################################################   
################################################################################################################################################################################ 

    def setup_grade_environment(self):
        
        if self.need_clear == True:
            self.clear_all_students()
        self.show_all_student()
        self.show_grade_options()
    
    def show_grade_options(self):
    
    
        self.subject_label = Label(self.add_grade, text = "Subject: ").grid(column=6,row=0,padx=(10,0),sticky=E)
        self.max_grade_label = Label(self.add_grade, text = "Max grade: ").grid(column=6,row=1,padx=(10,0),sticky=E)
        self.date_label = Label(self.add_grade, text = "Date: ").grid(column=6,row=2,padx=(10,0),sticky=E)
        
        self.subject = StringVar(self.add_grade, value=str(self.sql.get_professor_subject()))
        self.subject_entry = Entry(self.add_grade,textvariable=self.subject)
        self.subject_entry.grid(column=7,row=0)
        
        self.max_grade = IntVar(self.add_grade,value=20)
        self.max_grade_entry = Entry(self.add_grade,textvariable=self.max_grade)
        self.max_grade_entry.grid(column=7,row=1)
        
        date = datetime.datetime.now()
        str_date = str(date.day) + "/" + str(date.month) + "/" + str(date.year)
        self.date = StringVar(self.add_grade,value=str_date)
        self.date_entry = Entry(self.add_grade,textvariable=self.date)
        self.date_entry.grid(column=7,row=2)
    
    def show_all_student(self):
        
        self.student_list = self.sql.get_student_list(self.add_grade_classroom_entry.get())
         
        self.name_of_student = {}
        self.student_grade = {}
        student_grade_var = {}
        
        for i in range(len(self.student_list)):
            self.name_of_student[i] = Label(self.add_grade,text=str(self.student_list[i][0]))
            self.name_of_student[i].grid(column=4,row=0+i,sticky=E)
            student_grade_var[i] = IntVar()
            self.student_grade[i] = Entry(self.add_grade,textvariable = student_grade_var,width=4)
            self.student_grade[i].grid(column=5,row=0+i,sticky=E)
            
        self.need_clear = True
    
    def clear_all_students(self):
        
        for i in range(len(self.student_list)):
            self.name_of_student[i].destroy()
            self.student_grade[i].destroy()
        
      
        
    def verify_inputed_data(self):
        
        error = False
        
        ### test student grade < max grade
        for i in self.student_grade:
            if self.student_grade[i].get() == '':
                print("ERROR: you need to give a grade to all student")
                error = True
            elif int(self.student_grade[i].get()) > int(self.max_grade_entry.get()):
                print("ERROR: Grade n° " +  str(i+1) +" is more than max grade")
                error =True
            else:
                print("INFO: Valide grade")
        
        if error is False:
            self.sql.push_new_grade(1, self.add_grade_classroom_entry.get(), self.student_list, self.student_grade, self.max_grade_entry.get(), self.date_entry.get(), self.sql.get_professor_subject())     


#########################################################################################################################################################################################
################################################################################## SIGNAL ABSENCE PART ##################################################################################
#########################################################################################################################################################################################
   
   
   
        
    
class SQL:
    
    def __init__(self,professor_id):
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        self.professor_id = professor_id
        
    def get_student_list(self, classroom):
        data = (classroom,)
        self.c.execute('''SELECT nom,prenom,id_eleve FROM eleve WHERE classe = ? ORDER BY nom''',data)
        return self.c.fetchall()
    
    def get_professor_subject(self):
        data = (self.professor_id,)
        self.c.execute('''SELECT matiere FROM professor WHERE id = ?''',data)
        return self.c.fetchall()[0][0]

    def push_new_grade(self,id_devoir, classe, student_list, student_grade, note_max, date, matiere ):
        for i in range(len(student_list)):
            data = (id_devoir, classe, matiere, student_list[i][2], self.professor_id, int(student_grade[i].get()), note_max, date)
            self.c.execute('''INSERT INTO note VALUES (?,?,?,?,?,?,?,?)''',data)
        self.connexion.commit()
        print("INFO: Grades were added sucessfully")

def launch(id):
    root = Tk()
    sql = SQL(id)
    gui = GUI(root,sql)
    root.mainloop() 
   

    
   