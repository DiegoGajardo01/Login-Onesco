from tkinter import *
from tkinter import ttk
import mysql.connector


def salir():
    exit()

def formularioTaller():
    raiz =Tk()
    raiz.title("Onesco")
    raiz.geometry("1000x850")
    raiz.config(bg ="gray")
    raiz.config(bd="30")
    raiz.config(relief="groove")
    miframe = Frame(raiz,bg="white",width="1000", height="650")
    miframe.pack(fill ="both",expand = "True")

    nombrelable = Label(miframe,text ="Cuenta de Correo:",font =(16))
    nombrelable.grid(row="1",column="0")
    passlabel = Label(miframe,text ="Contraseña:",font =(16))
    passlabel.grid(row="2",column="0")
    agelabel = Label(miframe,text ="age:",font =(16))
    agelabel.grid(row="3",column="0")
    textocorreo= Entry(miframe,width="30")
    textocorreo.grid(row="1",column="1")
    textopass= Entry(miframe,width="30")
    textopass.grid(row="2",column="1")
    textoage= Entry(miframe,width="30")
    textoage.grid(row="3",column="1")
    iniciarSessionButton = Button(miframe, text="Salir", command=salir)
    iniciarSessionButton.grid(column=4, row=3,ipadx=5, ipady=5, padx=10, pady=10)


    cuentas = []
    def send_data():
        datos = {
            "Cuenta de Correo": textocorreo.get(),
            "Contraseña": textopass.get(),
            "age": textoage.get()
        }
        cuentas.append(datos)
    def iniciarSesion():
        print(cuentas)
    #Botones
    iniciarSessionButton = Button(miframe, text="Mostrar Datos", command=iniciarSesion)
    iniciarSessionButton.grid(row="11", column="2")

    ingresarboton = Button(miframe, text="Ingresar", command=send_data)
    ingresarboton.grid(row="11", column="1")
    raiz.mainloop()


def formularioRecepcion():
    raiz =Tk()
    raiz.title("Onesco")
    raiz.geometry("1000x850")
    raiz.config(bg ="gray")
    raiz.config(bd="30")
    raiz.config(relief="groove")
    miframe = Frame(raiz,bg="white",width="1000", height="650")
    miframe.pack(fill ="both",expand = "True")

    chasislable = Label(miframe,text ="Chasis:",font =(16))
    chasislable.grid(row="1",column="0")
    patentelabel = Label(miframe,text ="Patente:",font =(16))
    patentelabel.grid(row="2",column="0")
    modelolabel = Label(miframe,text ="Modelo:",font =(16))
    modelolabel.grid(row="3",column="0")
    marcalabel = Label(miframe,text ="Marca:",font =(16))
    marcalabel.grid(row="4",column="0")
    añolabel = Label(miframe,text ="Año:",font =(16))
    añolabel.grid(row="5",column="0")


    textChasis= Entry(miframe,width="30")
    textChasis.grid(row="1",column="1")
    textPatente= Entry(miframe,width="30")
    textPatente.grid(row="2",column="1")
    textModelo= Entry(miframe,width="30")
    textModelo.grid(row="3",column="1")
    textMarca= Entry(miframe,width="30")
    textMarca.grid(row="4",column="1")
    textAño= Entry(miframe,width="30")
    textAño.grid(row="5",column="1")
    iniciarSessionButton = Button(miframe, text="Salir", command=salir)
    iniciarSessionButton.grid(column=4, row=3,ipadx=5, ipady=5, padx=10, pady=10)


    cuentas = []
    def send_data():
        datos = {
            "Chasis": textChasis.get(),
            "Patente": textPatente.get(),
            "Modelo": textModelo.get(),
            "Marca": textMarca.get(),
            "Año": textAño.get()
        }
        cuentas.append(datos)
    def printData():
        print(cuentas)
    #Botones
    printDataButton = Button(miframe, text="Mostrar Datos", command=printData)
    printDataButton.grid(row="11", column="2")

    ingresarboton = Button(miframe, text="Guardar Datos", command=send_data)
    ingresarboton.grid(row="11", column="1")
    raiz.mainloop()

def tablaRecepcion():
    raiz =Tk()
    raiz.title("Onesco")
    raiz.geometry("1250x850")
    raiz.config(bg ="gray")
    raiz.config(bd="30")
    raiz.config(relief="groove")
    miframe = Frame(raiz,bg="gray",width="1000", height="650")
    miframe.pack(fill ="both",expand = "True")

    lista = ttk.Treeview( miframe, columns=(1,2,3,4,5,6), show="headings", height="8")
    
    lista.heading(1, text="Chasis")
    lista.heading(2, text="Patente")
    lista.heading(3, text="Modelo")
    lista.heading(4, text="Marca")
    lista.heading(5, text="Año")
    lista.heading(6, text="Precio")
    lista.heading(2, anchor=CENTER)

    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="onesco")
    cursor1=conexion1.cursor()
    sql = "select * from `onesco-recepcion-auto`"
    cursor1.execute(sql)
    a = cursor1.fetchall()
    print(a)
    for i in a:
        lista.insert('','end', values=i)
    cursor1.close()
    lista.place(x=1, y=90)


    
