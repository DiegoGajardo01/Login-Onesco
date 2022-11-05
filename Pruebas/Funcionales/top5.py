def top5():
    import mysql.connector

    conexion1=mysql.connector.connect(host="localhost", 
                                    user="root", 
                                    passwd="", 
                                    database="owo")
    cursor1=conexion1.cursor()

    cursor1.execute("SELECT puntos, id_user FROM user ORDER BY puntos DESC LIMIT 5")

    resultados= []

    for base in cursor1:
        result=list(base)
        result=result[0]
        resultados.append(result)

    conexion1.close()

    #imprimir resultados en una lista
    print(resultados)



top5()