import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="onesco")


#Simulamos la obtención de datos de la partida, usar solo para pruebas, luego borrar y hacer las conexiones con los reales
# puntos = random.randint(1000, 19999)
# id_user = random.randint(10000000, 99999999)
# reRaza = random.randint(0, 3)
# raza=['Lobo','Perro','Gato','Faraon']



consulta = "INSERT INTO `onesco_login`(`user`, `pass`) VALUES ('recepcion', 'recepcion1'),('taller', 'taller1')"
cursor1=conexion1.cursor()
cursor1.execute(consulta)
conexion1.commit()
conexion1.close()
# print(consulta)