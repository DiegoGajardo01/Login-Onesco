import mysql.connector

conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="onesco")
cursor1=conexion1.cursor()
def validarUser(usuario, contra):
    password = ""
    user = ""
    valid = None

    cursor1.execute(f"SELECT user FROM `onesco-login` WHERE user = '{usuario}' ")
    for base in cursor1:
        user=str(base)
        elim=['(',')',',',"'"]
        for i in elim:
            user = user.replace(i, '')
    

    cursor1.execute(f"SELECT pass FROM `onesco-login` WHERE user = '{usuario}' ")
    for base in cursor1:
        password=str(base)
        elim=['(',')',',',"'"]
        for i in elim:
            password = password.replace(i, '')
    if usuario == user and contra == password:
        return True
    else:
        return False
    conexion1.close()