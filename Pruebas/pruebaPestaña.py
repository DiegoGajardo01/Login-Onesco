from tkinter import *
from tkinter.ttk import Notebook, Style

raiz =Tk()
raiz.title("Onesco")
raiz.geometry("1000x850")
raiz.config(bg ="gray")
raiz.config(bd="30")
raiz.config(relief="groove")

nb = Notebook(raiz)
nb.pack(fill='both', expand='yes')

pes0 = Frame(nb)
pes1 = Frame(nb)

nb.add(pes0, text="Clientes")
nb.add(pes1, text="Autos")


Mysky = "#dac0f0"
Myyellow = "#F2C84B"

style = Style()


style.theme_create( "dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [200, 1], "background": Mysky },
            "map":       {"background": [("selected", Myyellow)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("dummy")


raiz.mainloop()