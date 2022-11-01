from tkinter import *
import formulario

def salir():
    exit()

def menuRecepcion():
    raiz1 =Tk()
    raiz1.title("Onesco")
    raiz1.geometry("1000x650")
    miframe = Frame(raiz1,bg="gray",width="1000", height="650")
    miframe.pack(fill ="both",expand = "True")

    ingresarDatosButton = Button(miframe, text="Ingresar Datos", command=formulario.formularioRecepcion, bg="#464646", fg="#fcfcfc")
    ingresarDatosButton.grid(column=2, row=3,ipadx=5, ipady=5, padx=10, pady=10)
    
    iniciarSessionButton = Button(miframe, text="Salir", command=salir, bg="#464646", fg="#fcfcfc")
    iniciarSessionButton.grid(column=4, row=3,ipadx=5, ipady=5, padx=10, pady=10)