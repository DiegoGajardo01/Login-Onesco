from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import ventanas


conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="onesco")

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
    preciolabel = Label(miframe,text ="Precio:",font =(16))
    preciolabel.grid(row="6",column="0")


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
    textPrecio= Entry(miframe,width="30")
    textPrecio.grid(row="6",column="1")
    
    def volver():
        raiz.withdraw()

    
    def send_data():
        Chasis = textChasis.get()
        Patente = textPatente.get()
        Modelo = textModelo.get()
        Marca = textMarca.get()
        Año = textAño.get()
        Precio = textPrecio.get()
        if Año.isdigit() == True and Precio.isdigit() == True:
            cursor1=conexion1.cursor()
            sql = "INSERT INTO `onesco_recepcion_auto`(`chasis`, `patente`, `modelo`, `marca`, `año`, `precio`) VALUES (%s,%s,%s,%s,%s,%s)"
            datos=(Chasis,Patente,Modelo,Marca,Año,Precio)
            cursor1.execute(sql, datos)
            conexion1.commit()
            conexion1.close()
            textChasis.delete(0, END)
            textPatente.delete(0, END)
            textModelo.delete(0, END)
            textMarca.delete(0, END)
            textAño.delete(0, END)
            textPrecio.delete(0, END)
            #textChasis.focus()  <-- Para hacer que esté esperando texto en chasis una vez enviado
        else:
            messagebox.showinfo(message="Hemos tenido problemas al intentar ingresar datos, por favor en AÑO y PRECIO introduce SOLO VALORES NUMERICOS, Sin Usar ni puntos ni comas", title="Problemas para ingresar datos")

    

    #Botones
    volverButton = Button(miframe, text="Volver", command=volver)
    volverButton.grid(column=7, row=3,ipadx=5, ipady=5, padx=10, pady=10)

    printDataButton = Button(miframe, text="Mostrar Datos", command=tablaRecepcion)
    printDataButton.grid(row="10", column="3")

    ingresarboton = Button(miframe, text="Guardar Datos", command=send_data)
    ingresarboton.grid(row="10", column="4")
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

    def volver():
        raiz.withdraw()

    lista = ttk.Treeview( miframe, columns=(1,2,3,4,5,6,7), show="headings", height="8")
    
    lista.column(1, width=100)
    lista.column(2, width=100)
    lista.column(3, width=100)
    lista.column(4, width=100)
    lista.column(5, width=100)
    lista.column(6, width=100)
    lista.column(7, width=100)

    lista.heading(1, text="Chasis", anchor=CENTER)
    lista.heading(2, text="Patente", anchor=CENTER)
    lista.heading(3, text="Modelo", anchor=CENTER)
    lista.heading(4, text="Marca", anchor=CENTER)
    lista.heading(5, text="Año", anchor=CENTER)
    lista.heading(6, text="Precio", anchor=CENTER)
    lista.heading(7, text="Dueño", anchor=CENTER)
    
    conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="onesco")

    cursor1=conexion1.cursor()
    sql = "select * from `onesco_recepcion_auto`"
    cursor1.execute(sql)
    a = cursor1.fetchall()
    for i in a:
        lista.insert('','end', values=i)
    lista.place(x=1, y=90)
    cursor1.close()

    volverButton = Button(miframe, text="Volver", command=volver)
    volverButton.grid(column=4, row=3,ipadx=5, ipady=5, padx=10, pady=10)