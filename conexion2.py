import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="onesco")

usuario = input("Ingresa Usuario:")
user = ""
cursor1=conexion1.cursor()
cursor1.execute(f"SELECT user FROM `onesco-login` WHERE user = '{usuario}' ")
for base in cursor1:
    user=str(base)
    elim=['(',')',',',"'"]
    for i in elim:
        user = user.replace(i, '')
if usuario == user:
    valid = True
else:
    valid = False
    
conexion1.close()