import os 
os.system('pip install mysql-connector-python')
os.system('cls')

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
        cursor1.execute("CREATE TABLE `owo`.`user` ( `id` INT NOT NULL AUTO_INCREMENT , `nombre` VARCHAR(100) NOT NULL , `raza` VARCHAR(50) NOT NULL , `puntaje` INT NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")



    conexion1.close()

creaBD()