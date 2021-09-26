# La programacion modular se expresa a traves de decoradores
# La programacion estructurada se expresa a traves de la ejecucion del codigo linea n+1
# El control de flujo se hace a traves de la identacion y manteniendo la programacion estructurada


numOne= int(input("ingrese primer numero: "))
numTwo = int(input("ingrese segundo numero: "))

if ( numOne > numTwo) :
    print("El numero ", numOne, "es mayor a ", numTwo)
elif (numOne == numTwo ):
    print("Los numeros " , numOne, " y ", numTwo, "Son iguales")
else:
    print("El numero ", numOne, "es menor a ", numTwo)


print("La tabla de multiplicacion del numero ", numOne, " es ")
for i in range(0, 10):
    print( numOne, " x ", i , " = ", i*numOne)

def decorador(func):
    print("Entrada al modulo")
    return func

@decorador
def Numero():
    print("No ejecuta bucle o condicional dentro de la funcion decorador")

Numero()