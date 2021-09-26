
priLado = int(input("ingrese primer lado: "))
segLado = int(input("ingrese segundo lado: "))
terLado = int(input("ingrese tercer lado: "))

def decorador(func):
    print("Entrada al modulo")
    return func

@decorador
def Triangulo():
    print("Los lados indican que el triangulo es ", end="")
    if ( priLado == segLado == terLado):
        print("equilatero")
    elif (priLado == segLado or priLado == terLado or segLado == terLado):
        print("isósceles")
    else:
        print("escaleno")

Triangulo()
