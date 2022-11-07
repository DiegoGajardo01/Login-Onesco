from tkinter import *
import formulario


def salir():
    exit()

def menuRecepcion():
    raiz1 =Tk()
    raiz1.title("Onesco")
    raiz1.geometry("480x220")
    raiz1.iconbitmap("medios/Auto.ico")
    miframe = Frame(raiz1,bg="gray",width="480", height="220")
    miframe.pack(fill ="both",expand = "True")

    ingresarDatosButton = Button(miframe, text="Ingresar Datos Cliente", command=formulario.formularioRecepcion, bg="#464646", fg="#fcfcfc")
    ingresarDatosButton.grid(column=2, row=3,ipadx=5, ipady=5, padx=30, pady=80)

    mostrarDatosButton = Button(miframe, text="Mostrar Datos", command=formulario.tablaRecepcion, bg="#464646", fg="#fcfcfc")
    mostrarDatosButton.grid(column=6, row=3,ipadx=5, ipady=5, padx=30, pady=80)
    
    iniciarSessionButton = Button(miframe, text="Salir", command=salir, bg="#464646", fg="#fcfcfc")
    iniciarSessionButton.grid(column=4, row=3,ipadx=5, ipady=5, padx=30, pady=80)