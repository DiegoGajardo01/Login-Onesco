import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="onesco")


cursor1=conexion1.cursor()
cursor1.execute("DROP DATABASE onesco")
conexion1.commit()
conexion1.close()