print("Ejercicio con Tupla y lista:  ")

tupla = (13, 1, 8, 3, 2, 5, 8)
listaTupla = list(tupla)

nuevaLista =[]

#Ordenamiento de burbuja
ban = False
while ban == False:
    ban = True
    for num1 in range(len(listaTupla)-1):
        if listaTupla[num1] > listaTupla[num1 + 1]:
            aux = listaTupla[num1]
            listaTupla[num1] = listaTupla[num1 + 1]
            listaTupla[num1 + 1] = aux
            ban = False

tupla = tuple(listaTupla)

for numero in listaTupla:
    if numero < 5:
        nuevaLista.append(numero)
        print(numero)
else:
    print("Fin de la lista")



