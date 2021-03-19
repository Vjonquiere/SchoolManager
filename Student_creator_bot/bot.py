import random
import sqlite3
import hashlib
import configparser

connexion = sqlite3.connect('login.db')
c = connexion.cursor()

#### CREATION DES TABLES NECESSAIRES ####
c.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, mdp TEXT, role TEXT) ;''')
c.execute('''CREATE TABLE IF NOT EXISTS eleve(id_eleve INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, niveau INTEGER, classe TEXT, nbr_absence INTEGER, demi_pens TEXT)  ''')
c.execute('''CREATE TABLE IF NOT EXISTS school_office(id_vie_sco INTEGER PRIMARY KEY, nom TEXT, prenom TEXT)  ''')
c.execute('''CREATE TABLE IF NOT EXISTS absence(id INTEGER PRIMARY KEY AUTOINCREMENT, eleve_id INTEGER, debut DATETIME, fin DATETIME, justification_valide BOOLEAN)''')
c.execute('''CREATE TABLE IF NOT EXISTS professor(id INTEGER PRIMARY KEY, nom TEXT, prenom TEXT, matiere TEXT, matiere2 TEXT, demi_pens BOOLEAN)''')
c.execute('''CREATE TABLE IF NOT EXISTS note(id_devoir INTEGER, classe TEXT, matiere TEXT, eleve_id INTEGER, prof_id INTEGER, note INTEGER, note_max INTEGER, date DATE)''')
c.execute('''CREATE TABLE IF NOT EXISTS prof_classe(prof_id INTEGER, classe1 TEXT, classe2 TEXT, classe3 TEXT, classe4 TEXT, classe5 TEXT)''')


config = configparser.ConfigParser()
config.read('config.ini')


def create_name_list(family_name_list="Family-Names.txt", name_list="NAMES.txt"):

    family_name_file = open("Family-Names.txt", "r")
    list_of_family_name = []
    for line in family_name_file:
      stripped_line = line.strip()
      list_of_family_name.append(stripped_line)
     
    name_file = open("Family-Names.txt", "r")
    list_of_name = []
    for line in name_file:
      name_stripped_line = line.strip()
      list_of_name.append(name_stripped_line)
      
    final_list = []
    final_list.append(list_of_family_name)
    final_list.append(list_of_name)
    
    family_name_file.close()
    name_file.close()
    
    return final_list

toutes_les_listes = create_name_list()

def student_adder(classroom):
    
        nom = random.choice(toutes_les_listes[0])
        prenom = random.choice(toutes_les_listes[1])
        niveau = 3
        classe = classroom        
        dp = True
        
        nbr_absence = 0
        login = prenom.lower() + "." + nom.lower()           
        mdp = mdp_generateur()
        txt_creator(nom,prenom,classe,login,mdp)
        hash_mdp = hashlib.md5(mdp.encode()).hexdigest()
        
        data_login = (login, hash_mdp,)
        c.execute('''INSERT INTO users VALUES (NULL,?,?,"eleve")''',data_login)
        connexion.commit()
    
        eleve_id = get_id(login)
        data_person = (eleve_id,nom,prenom,niveau,classe,nbr_absence,dp)
        c.execute('''INSERT INTO eleve VALUES (?,?,?,?,?,?,?)''',data_person)
        connexion.commit()
        
        mdp = ""


def get_id(login):
    data = (login,)
    c.execute('''SELECT id FROM users WHERE login = ? ''', data)
    a = c.fetchall()
    return a[0][0]
    
    
def mdp_generateur():
    mdp = ""
    for i in range(8):
        add = random.choice(["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","1","2","3","4","5","6","7","8","9","*","/","!"])
        mdp = mdp + add
    return mdp

def txt_creator(nom,prenom,classe,login,mdp):
    file_name = nom + "." + prenom + ".txt"
    file1 = open(file_name,"w+")
    file1.write("|------------------------------------------|\n|        Access code School Manager        |\n\n    student: " + nom + " " + prenom + " " + classe + "\n\n    username: " + login + "\n    password: " + mdp + "\n\n|------------------------------------------|")
    file1.close()


for l in range(int(config['classroom']['number_of_level'])):    
    for k in range(len(config['classroom']['level_{}_class'.format(l+1)].split(","))):
        for i in range(int(int(config['classroom_setup']['level_{}_student_number'.format(l+1)])/len(config['classroom']['level_{}_class'.format(l+1)].split(",")))):
            print(config['classroom']['level_{}_class'.format(l+1)].split(","))
            student_adder(str(config['classroom']['level_{}_class'.format(l+1)].split(",")[k-1]))
