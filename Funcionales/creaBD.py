import os 
os.system('pip install mysql-connector-python')


import mysql.connector
def creaBD():

    tablas=[]

    conexion1=mysql.connector.connect(host='localhost', user='root', passwd='')
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
        cursor1.execute("CREATE TABLE `onesco`.`onesco_login` (`id` INT NOT NULL AUTO_INCREMENT , `user` VARCHAR(45) NOT NULL , `pass` VARCHAR(45) NOT NULL , PRIMARY KEY (`id`)) ENGINE = InnoDB;")
        cursor1.execute("CREATE TABLE `onesco`.`onesco_recepcion_clientes` (`rut_cliente` VARCHAR(10) NOT NULL , `nombre_cliente` VARCHAR(50) NOT NULL , `contacto` VARCHAR(45) NOT NULL , PRIMARY KEY (`rut_cliente`)) ENGINE = InnoDB;")
        cursor1.execute("CREATE TABLE `onesco`.`onesco_autos` (`chasis` VARCHAR(60) NOT NULL , `patente` VARCHAR(45) NOT NULL , `modelo` VARCHAR(45) NOT NULL , `marca` VARCHAR(45) NOT NULL , `año` INT NOT NULL , `kilometraje` INT NOT NULL , `precio` INT NOT NULL , `precio_final` INT NOT NULL , `estado` BOOLEAN NOT NULL , PRIMARY KEY (`chasis`))  ENGINE = InnoDB;")
        cursor1.execute("alter table `onesco`.`onesco_autos` add rut_dueño VARCHAR(10) not null ;")
        cursor1.execute("alter table `onesco`.`onesco_autos` add constraint `FK_cliente_autos` foreign key (`rut_dueño`) references `onesco_recepcion_clientes` (`rut_cliente`) ON DELETE CASCADE ON UPDATE CASCADE;")
    conexion1.close()

creaBD()