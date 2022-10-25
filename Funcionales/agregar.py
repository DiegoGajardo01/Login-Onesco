import mysql.connector
import random
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="owo")


#Simulamos la obtención de datos de la partida, usar solo para pruebas, luego borrar y hacer las conexiones con los reales
puntos = random.randint(1000, 19999)
id_user = random.randint(10000000, 99999999)
reRaza = random.randint(0, 3)
raza=['Lobo','Perro','Gato','Faraon']



consulta = "INSERT INTO `user`(`id_user`, `raza`, `puntos`) VALUES ('{}', '{}', {})".format(id_user, raza[reRaza], puntos)
cursor1=conexion1.cursor()
cursor1.execute(consulta)
conexion1.commit()
conexion1.close()
# print(consulta)