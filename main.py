#Imports
from tkinter import *
import conexion
import formulario
import ventanas
from tkinter import messagebox

root = Tk()
nombreUser = StringVar()
passUser = StringVar()


def createGUI():
    #Ventana Main
    root.title("Login")
    root.config(bg="#4F518C")

    #Main Frame
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=480, height=320, bg="#353535")

    #Etiqueta de texto
    titulo = Label(mainFrame, text="Login de Usuario Onesco", font=("Arial",24), bg="#353535", fg="#fcfcfc")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    #Textos
    userLabel = Label(mainFrame, text="Usuario: ", bg="#353535", fg="#fcfcfc")
    userLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Contraseña: ", bg="#353535", fg="#fcfcfc")
    passLabel.grid(column=0, row=3)

    #Inputs
    nombreUser.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUser, width=40, bg="#8b8b8b")
    nombreEntry.grid(column=0, row=2, columnspan=2)

    passUser.set("")
    passEntry = Entry(mainFrame, textvariable=passUser, show="*", width=40, bg="#8b8b8b")
    passEntry.grid(column=0, row=4, columnspan=2)

    #Botones
    iniciarSessionButton = Button(mainFrame, text="Ingresar", command=iniciarSesion, bg="#464646", fg="#fcfcfc")
    iniciarSessionButton.grid(column=1, row=5,ipadx=5, ipady=5, padx=10, pady=10)
    
    
    root.mainloop()

def iniciarSesion():
    continuar = conexion.validarUser(nombreUser.get(), passUser.get())
    if continuar == True:
        root.withdraw()

        if nombreUser.get() == "recepcion":
            ventanas.menuRecepcion()
        elif nombreUser.get() == "taller":
            formulario.formularioTaller()
    else:
        messagebox.showinfo(message="Hemos tenido problemas al intentar solucionar tu login, intenta ingresar correctamente los datos", title="Problemas para ingresar")

def salir():
    exit()


if __name__== "__main__":
    createGUI()