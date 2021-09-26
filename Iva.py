total = int(input("Ingresar el total de lo facturado: "))
iva = 0
print(iva)

def Total(iva = 0.21):
    ivaIngresado = input("Ingresar el iva o presione enter para continuar: ")

    if( ivaIngresado == ''):
        print(iva)
        iva = 1 + 0.21
    else:
        print(ivaIngresado)
        iva = float(ivaIngresado )+ 1

    return(total * iva)

print("El total es: ",Total())