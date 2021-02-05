from tkinter import *
import sqlite3


class GUI:
    def __init__(self, master, id,sql_db):
        
        self.m = master
        self.m.minsize(900,250)
        self.sql = sql_db


class SQL:
    def __init__(self,id_school_office):
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        self.id_school_office = id_school_office


def launch(id):
    sql_connexion = SQL(id)
    root = Tk()
    my_gui = GUI(root,id, sql_connexion)
    root.mainloop()