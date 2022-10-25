import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="owo")


cursor1=conexion1.cursor()
cursor1.execute("DROP DATABASE owo")
conexion1.commit()
conexion1.close()