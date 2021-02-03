from tkinter import *
import sqlite3,hashlib,sys,random

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.minsize(300,250)
        self.master.maxsize(300,250)
        
        self.connexion = sqlite3.connect('login.db')
        self.c = self.connexion.cursor()
        
        
        self.mdp = ""
        
        #### CREATION DES TABLES NECESSAIRES ####
        self.c.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, mdp TEXT, role TEXT) ;''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS eleve(id_eleve INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, niveau INTEGER, classe TEXT, nbr_absence INTEGER, demi_pens TEXT)  ''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS school_office(id_vie_sco INTEGER PRIMARY KEY, nom TEXT, prenom TEXT)  ''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS absence(id INTEGER PRIMARY KEY AUTOINCREMENT, eleve_id INTEGER, debut DATETIME, fin DATETIME, justification_valide BOOLEAN)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS professor(id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, matiere TEXT, matiere2 TEXT, demi_pens BOOLEAN)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS note(id_devoir INTEGER, classe TEXT, matiere TEXT, eleve_id INTEGER, prof_id INTEGER, note INTEGER)''')
        self.c.execute('''CREATE TABLE IF NOT EXISTS prof_classe(prof_id INTEGER, classe1 TEXT, classe2 TEXT, classe3 TEXT, classe4 TEXT, classe5 TEXT)''')
        
        self.selector()
    
    def selector(self):
        while True:
            self.menu1 = input("ajouter eleve -> a \najouter vie sco -> b \njustifier absence -> c \n \n ->  ")
            if self.menu1 == "a":
                self.student_adder()
            if self.menu1 == "b":
                self.school_office_adder()
            if self.menu1 == "c":
                sys.quit()
    
      
    def student_adder(self):
        
        #### Inputable required values
        
            self.nom = input("nom: ")
            self.prenom = input("prenom: ")
            self.niveau = input("niveau: ")
            self.classe = input("classe: ")          
            self.dp = input("demi-pensionnaire : ")
        
        ### Other Values
            
            self.nbr_absence = 0
            self.login = self.prenom.lower() + "." + self.nom.lower()           
            self.mdp_generateur()
            self.txt_creator()
            self.hash_mdp = hashlib.md5(self.mdp.encode()).hexdigest()
            
        
        #### User creation
        
            self.data_login = (self.login, self.hash_mdp,)
            self.c.execute('''INSERT INTO users VALUES (NULL,?,?,"eleve")''',self.data_login)
            self.connexion.commit()
        
        ### student creation
            self.eleve_id = self.get_id()
            self.data_person = (self.eleve_id,self.nom,self.prenom,self.niveau,self.classe,self.nbr_absence,self.dp)
            self.c.execute('''INSERT INTO eleve VALUES (?,?,?,?,?,?,?)''',self.data_person)
            self.connexion.commit()
            
            self.mdp = ""

    
    def mdp_generateur(self):
        for i in range(8):
            add = random.choice(["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","1","2","3","4","5","6","7","8","9","*","/","!"])
            self.mdp = self.mdp + add
            
        print(self.mdp)
        
        
    def txt_creator(self):
        file_name = self.nom + self.prenom + ".txt"
        file1 = open(file_name,"w+")
        file1.write("|------------------------------------------|\n|        Access code School Manager        |\n\n    student: " + self.nom + " " + self.prenom + " " + self.classe + "\n\n    username: " + self.login + "\n    password: " + self.mdp + "\n\n|------------------------------------------|")
        file1.close()
     
    def school_office_adder(self):
        
        #### Inputable required values
        
            self.nom = input("nom: ")
            self.prenom = input("prenom: ")

        
        ### Other Values
            
            self.login = self.prenom.lower() + "." + self.nom.lower()           
            self.mdp_generateur()
            self.txt_creator()
            self.hash_mdp = hashlib.md5(self.mdp.encode()).hexdigest()
            
        
        #### User creation
        
            self.data_login = (self.login, self.hash_mdp,)
            self.c.execute('''INSERT INTO users VALUES (NULL,?,?,"school_office")''',self.data_login)
            self.connexion.commit()
        
        ### school office account creator
            self.school_office_id = self.get_id()
            self.data_person = (self.school_office_id,self.nom,self.prenom)
            self.c.execute('''INSERT INTO school_office VALUES (?,?,?)''',self.data_person)
            self.connexion.commit()
            
            self.mdp = ""
        
    def get_id(self):
        self.data = (self.login,)
        self.c.execute('''SELECT id FROM users WHERE login = ? ''', self.data)
        self.a = self.c.fetchall()
        return self.a[0][0]
        
           
root = Tk()
my_gui = GUI(root)
root.mainloop()