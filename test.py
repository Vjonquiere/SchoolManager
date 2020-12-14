import sqlite3

connexion = sqlite3.connect('login.db')
c = connexion.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY AUTOINCREMENT, login TEXT, mdp TEXT, role TEXT);''')
c.execute('''INSERT INTO person VALUES (NULL,"yo","les","eleve")''')
connexion.commit()