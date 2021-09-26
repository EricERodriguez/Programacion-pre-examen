def Transpilador(decimal):
    # parte binaria
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2

    return "Binario: " + str(decimal) + binario

def ChangeHex(numero):
    if (numero < 0):
        print(0)
    elif (numero<=1):
        print("Hex : ", end="")
    else:
        ChangeHex( numero / 16 )
        x =(numero%16)
        if (x < 10):
            print(x),
        if (x == 10):
            print("a", end=""),
        if (x == 11):
            print("b", end=""),
        if (x == 12):
            print("c", end=""),
        if (x == 13):
            print("d", end=""),
        if (x == 14):
            print("e", end=""),
        if (x == 15):
            print ("f", end=""),

numero = int(input('Introduce el número a convertir a binario y hexadecimal: '))

print(Transpilador(numero))
print(ChangeHex(numero))

binarios = bin(numero)
hexadecimal = hex(numero)
print("Comparar con metodo py binario : ",binarios[slice(2,len(binarios))])
print("Comparar con metodo py hex : ",hexadecimal[slice(2,len(hexadecimal))])

