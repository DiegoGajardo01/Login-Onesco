def limpiarPuntos(rut):
    caracteres = "1234567890-k"
    rutx = ""
    for cambio in rut.lower():
        if cambio in caracteres:
            rutx += cambio
    if rutx.find("-") == -1:
        
        preRut=rutx[:-1]
        postRut=rutx[-1:]
        rutx=preRut+ "-"+postRut
        return rutx
    else:
        return rutx

ruti = "211324880"
ruti2 = "21.132.488-0"
print(limpiarPuntos(ruti))
print(limpiarPuntos(ruti2))