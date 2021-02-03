import sqlite3
import datetime 
import time
import random


#INSERT INTO absence VALUES (1,1,"2021-1-23 18:42:25","2021-1-23 18:42:26",True)

connexion = sqlite3.connect('login.db')
c = connexion.cursor()
#c.execute('''CREATE TABLE IF NOT EXISTS absence(id INTEGER PRIMARY KEY, debut DATETIME, fin DATETIME, justification BOOLEAN );''')

date = datetime.datetime.now()
a = str(date.year) + "-" + str(date.month) + "-" + str(date.day) + " " + str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
print(a)


#################################################################################################

mdp = ""
for i in range(8):
    add = random.choice(["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n","A","Z","E","R","T","Y","U","I","O","P","Q","S","D","F","G","H","J","K","L","M","W","X","C","V","B","N","1","2","3","4","5","6","7","8","9","*","/","!"])
    mdp = mdp + add
print(mdp)


#################################################################################################
username = "gg"

file1 = open("test.txt","w+")
file1.write("|------------------------------------------|\n|        Access code School Manager        |\n\n    username: " + username + "\n    password: " + mdp + "\n|------------------------------------------|")
file1.close()


##################################################################################################

data = ("",)
c.execute('''SELECT id FROM users WHERE login = ? ''', data)
a = c.fetchall() 
print(a[0][0])