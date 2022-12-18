print("Numeros divisibles entre 3 del 1 al 10")

print("Establecemos una lista ")

listaNumeros:list = [1,2,3,4,5,6,7,8,9]
listaNumeros.append(10)

print(f"Salida de lista : {listaNumeros}")

for numero in listaNumeros:
    if numero % 3 == 0:
        print(f"Numero Divisible entre Tres : {numero}")


else: print("Fin del ciclo")

