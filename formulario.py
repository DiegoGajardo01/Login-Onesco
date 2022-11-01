from tkinter import *
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

    nombrelable = Label(miframe,text ="Chasis:",font =(16))
    nombrelable.grid(row="1",column="0")
    passlabel = Label(miframe,text ="rut:",font =(16))
    passlabel.grid(row="2",column="0")
    agelabel = Label(miframe,text ="marca:",font =(16))
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
