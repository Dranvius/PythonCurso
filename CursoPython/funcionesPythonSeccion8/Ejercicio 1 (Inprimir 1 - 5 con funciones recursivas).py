print("Salida por consola con funcion recursiva  y una función soporte: ")

numPositivo = int(input("Inserte un Numero positivo : "))

#Construcción de Array por medio de un numero
def construccionArray (num):
    array = []
    while num > 0:
        array.append(num)
        num -= 1
    return array


#Funcion recursiva para la salida de datos
def salidaPantalla (lista, bandera=True):
    if bandera == True:
        for numero in range(salidaPantalla(construccionArray(numPositivo),bandera = False)):
            print(lista[numero])
    elif bandera == False:
        return len(construccionArray(numPositivo))


salidaPantalla(construccionArray(numPositivo))


