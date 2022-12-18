print("Ejercicio para multiplicar las parametros de variables : ")

#Multiplicacion con una varialble arg como parametro
#Ejercicio 1
print("Multiplicación del Args con un numero")
def multiplicacionesDeVaribles(*tupla,num):
    for numero in tupla:
        print(numero * num)

multiplicacionesDeVaribles(1,2,3,4,5,6,num=5)

#Ejercicio 2

def multiplicaciónDeTodosArgs(*args):
    num = 1
    for numero in args:
        num *= numero
        print(num)

print("Multiplicacion del Args : ")

multiplicaciónDeTodosArgs(1,2,3,4,5,6,7)

#Ejercicio 3
print("----------------------")
#Ejercicio con un objete entrada

tupla3 = (1,2,3,4,5,6)

def recorridoBasico(tupla):
    for numero in tupla:
        print(numero)

recorridoBasico(tupla3)