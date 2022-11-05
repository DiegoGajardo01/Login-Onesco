from tkinter import *
from tkinter import ttk

raiz =Tk()
raiz.title("Onesco")
raiz.geometry("1000x850")
raiz.config(bg ="gray")
raiz.config(bd="30")
raiz.config(relief="groove")


nb = ttk.Notebook(raiz)
nb.pack(fill='both', expand='yes')
pes0 = ttk.Frame(nb)
pes1 = ttk.Frame(nb)

nb.add(pes0, text="Clientes")
nb.add(pes1, text="Autos")
raiz.mainloop()