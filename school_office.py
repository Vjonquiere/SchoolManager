from tkinter import *

import sqlite3
import datetime
from PIL import ImageTk 

class GUI:
    def __init__(self, master, id,sql_db):
        
        self.m = master
        self.m.minsize(900,250)
        self.sql = sql_db
        
        self.add_absence_frame = Frame(self.m)
        self.add_absence_frame.grid(row=0,column=0,pady=(30,0),padx=(10,0))
        
        self.absence_adder_widget()
        self.show_classroom_student()


    def absence_adder_widget(self):
        date = datetime.datetime.now()
        
        self.classroom_label = Label(self.add_absence_frame,text = "Classroom :").grid(column=0,row=0,sticky=N,pady=(5,0))
        
        self.classroom = StringVar()
        self.classroom_entry= Entry(self.add_absence_frame,textvariable = self.classroom, width = 10) 
        self.classroom_entry.grid(row=0,column=1,sticky=N,pady=(5,0))
        
        self.search_classroom = Button(self.add_absence_frame,text="Search",command= self.show_classroom_student).grid(row=0,column=2,sticky=N)
        
        self.since_label = Label(self.add_absence_frame, text="Since: ").grid(column=4,row=0,sticky=N)
        self.until_label = Label(self.add_absence_frame, text="Until: ").grid(column=4,row=1,sticky=N)
        
        self.img = ImageTk.PhotoImage(master = self.add_absence_frame,file="icons/icon_add.png")
        self.but = Button(self.add_absence_frame, text = 'Add absence', image = self.img, compound = LEFT,height=10).grid(column=13,row=0,sticky=N)
        
        ### all spinbox for date/time of abscence
        self.label_slash = Label(self.add_absence_frame,text=" / ").grid(column=6,row=0,sticky=N)
        self.label_slash2 = Label(self.add_absence_frame,text=" / ").grid(column=8,row=0,sticky=N)
        self.label_slash3 = Label(self.add_absence_frame,text=" h ").grid(column=11,row=0,sticky=N)
        day = StringVar(self.add_absence_frame,value=date.day)
        mounth = StringVar(self.add_absence_frame,value=date.month)
        year = StringVar(self.add_absence_frame,value=date.year)
        hour = StringVar(self.add_absence_frame,value=date.hour)
        minute = StringVar(self.add_absence_frame,value=date.minute)
        self.since_day = Spinbox(self.add_absence_frame,textvariable=day,from_=1,to=31,width=2).grid(column=5,row=0,sticky=N)
        self.since_mounth = Spinbox(self.add_absence_frame,textvariable=mounth,from_=1,to=12, width=2).grid(column=7,row=0,sticky=N)
        self.since_year = Spinbox(self.add_absence_frame,textvariable=year,from_=2020,to=2050, width=4).grid(column=9,row=0,sticky=N)
        self.since_hour = Spinbox(self.add_absence_frame,textvariable=hour,from_=0,to=23, width=4).grid(column=10,row=0,padx=(20,0),sticky=N)
        self.since_minute = Spinbox(self.add_absence_frame,textvariable=minute,from_=0,to=59, width=4).grid(column=12,row=0,sticky=N)
        
        self.label_slash4 = Label(self.add_absence_frame,text=" / ").grid(column=6,row=1,sticky=N)
        self.label_slash5 = Label(self.add_absence_frame,text=" / ").grid(column=8,row=1,sticky=N)
        self.label_slash6 = Label(self.add_absence_frame,text=" h ").grid(column=11,row=1,sticky=N)
        day_until = StringVar(self.add_absence_frame,value=date.day)
        mounth_until = StringVar(self.add_absence_frame,value=date.month)
        year_until = StringVar(self.add_absence_frame,value=date.year)
        hour_until = StringVar(self.add_absence_frame,value=date.hour)
        minute_until = StringVar(self.add_absence_frame,value=date.minute)
        self.until_day = Spinbox(self.add_absence_frame,textvariable=day_until,from_=1,to=31,width=2).grid(column=5,row=1,sticky=N)
        self.until_mounth = Spinbox(self.add_absence_frame,textvariable=mounth_until,from_=1,to=12, width=2).grid(column=7,row=1,sticky=N)
        self.until_year = Spinbox(self.add_absence_frame,textvariable=year_until,from_=2020,to=2050, width=4).grid(column=9,row=1,sticky=N)
        self.until_hour = Spinbox(self.add_absence_frame,textvariable=hour_until,from_=0,to=23, width=4).grid(column=10,row=1,padx=(20,0),sticky=N)
        self.until_minute = Spinbox(self.add_absence_frame,textvariable=minute_until,from_=0,to=59, width=4).grid(column=12,row=1,sticky=N)
      
    def show_classroom_student(self):
        
        student_list = self.sql.get_classroom_student(self.classroom_entry.get())
        self.student_list_show = Listbox(self.add_absence_frame,width=8,height=len(student_list))
        
        for i  in range(len(student_list)):
            self.student_list_show.insert(i, str(student_list[i][0]))
        
        self.student_list_show.grid(column=3,row=0,padx=10,pady=(5,0))
        

        
class SQL:
    def __init__(self,id_school_office):
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        self.id_school_office = id_school_office

    def get_classroom_student(self, classroom):
        self.data = (classroom,)
        self.c.execute('''SELECT nom,prenom FROM eleve WHERE classe = ? ''', self.data)
        return self.c.fetchall() 

def launch(id):
    sql_connexion = SQL(id)
    root = Tk()
    my_gui = GUI(root,id, sql_connexion)
    root.mainloop()