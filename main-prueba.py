#Imports
from cgitb import text
from tkinter import *
import conexion
import formulario
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
    mainFrame.config(width=480, height=320, bg="#907AD6")

    #Etiqueta de texto
    titulo = Label(mainFrame, text="Login de Usuario Onesco", font=("Arial",24), bg="#907AD6", fg="#7FDEFF")
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
    #Textos
    userLabel = Label(mainFrame, text="User: ", bg="#907AD6", fg="#7FDEFF")
    userLabel.grid(column=0, row=1)
    passLabel = Label(mainFrame, text="Password: ", bg="#907AD6", fg="#7FDEFF")
    passLabel.grid(column=0, row=2)

    #Inputs
    nombreUser.set("")
    nombreEntry = Entry(mainFrame, textvariable=nombreUser)
    nombreEntry.grid(column=1, row=1)

    passUser.set("")
    passEntry = Entry(mainFrame, textvariable=passUser, show="*")
    passEntry.grid(column=1, row=2)

    #Botones
    iniciarSessionButton = Button(mainFrame, text="Iniciar Sesión", command=iniciarSesion)
    iniciarSessionButton.grid(column=1, row=3,ipadx=5, ipady=5, padx=10, pady=10)
    
    
    root.mainloop()

def iniciarSesion():
    continuar = conexion.validarUser(nombreUser.get(), passUser.get())
    if continuar == True:
        root.withdraw()

        if nombreUser.get() == "recepcion":
            print(1)
        elif nombreUser.get() == "taller":
            print(2)
            tallerWd = Toplevel()
            tallerWd.title("Menu Taller")
            tallerWd.config(width=480, height=320, bg="#907AD6")
            tallerWd.geometry("640x480")
            #Botones
            iniciarSessionButton = Button(tallerWd, text="Salir", command=salir)
            iniciarSessionButton.grid(column=1, row=3,ipadx=5, ipady=5, padx=10, pady=10)        
    else:
        messagebox.showinfo(message="Hemos tenido problemas al intentar solucionar tu login, intenta ingresar correctamente los datos", title="Problemas para ingresar")

def salir():
    exit()


if __name__== "__main__":
    createGUI()

