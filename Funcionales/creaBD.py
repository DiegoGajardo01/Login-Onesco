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
    onesco = 'onesco' in tablas
    if onesco == False:
        cursor1.execute("CREATE DATABASE onesco")
        cursor1.execute("CREATE TABLE `onesco`.`onesco-login` (`id` INT NOT NULL AUTO_INCREMENT , `user` VARCHAR(45) NOT NULL , `pass` VARCHAR(45) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")



    conexion1.close()

creaBD()