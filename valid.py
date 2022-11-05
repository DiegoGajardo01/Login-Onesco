def validarRut(rut):
    caracteres = "1234567890k"
    rutx = ""
    for cambio in rut.lower():
        if cambio in caracteres:
            rutx += cambio
    rfiltro = rutx
    rutx = str(rfiltro[0:len(rfiltro)-1])
    digito = str(rfiltro[-1])
    multiplo = 2
    total = 0
    for reverso in reversed(rutx):
        total += int(reverso) * multiplo
        if multiplo == 7:
            multiplo = 2
        else:
            multiplo += 1
        modulus = total % 11
        verificador = 11 - modulus
        if verificador == 10:
            div = "k"
        elif verificador == 11:
            div = "0"
        else:
            if verificador < 10:
                div = verificador
    if str(div) == str(digito):
        caracteres = "1234567890k"
        rutx2 = ""
        for cambio in rut.lower():
            if cambio in caracteres:
                rutx2 += cambio
        preRut=rutx2[:-1]
        postRut=rutx2[-1:]
        rut=preRut+ "-"+postRut
        return rut
    else:
        pass