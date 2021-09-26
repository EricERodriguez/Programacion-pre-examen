def ChangeHex(numero):
    if (numero < 0):
        print(0)
    elif (numero<=1):
        print(numero)
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