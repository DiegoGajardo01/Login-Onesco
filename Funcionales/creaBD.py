import os 
os.system('pip install mysql-connector-python')


import mysql.connector
def creaBD():

    tablas=[]

    conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
    cursor1=conexion1.cursor()
    cursor1.execute("show databases")

    for base in cursor1:
        tabla=str(base)
        elim=['(',')',',',"'"]
        for i in elim:
            tabla = tabla.replace(i, '')
        tablas.append(tabla)
        


    #Comprobamos si está la base de datos del user creada
    owo = 'owo' in tablas
    if owo == False:
        cursor1.execute("CREATE DATABASE owo")
        cursor1.execute("CREATE TABLE `owo`.`user` ( `id_user` VARCHAR(255) NOT NULL , `raza` VARCHAR(100) NOT NULL , `puntos` INT NOT NULL , PRIMARY KEY (`id_user`(255))) ENGINE = InnoDB;")



    conexion1.close()

creaBD()