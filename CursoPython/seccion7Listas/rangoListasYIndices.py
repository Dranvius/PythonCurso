print("Rangos de listas para controlar")

listaNueva:list = ["Alexis","Sergio","Napy","Nayomi"]


print("Salida por consola de lista : \n")
print(listaNueva)

print("Salida por consola de una lista en rango : ")
print(listaNueva[0 : 2]) #Imprime desde la posición cero hasta la 1 sin tomar la 2
print(listaNueva[2 : 4]) #Salida de Napy y Nayomi (Ojo con los indices)
                #[Desde : hasta sin tomarlo]

print("\nOtra salida sin indice 'desde' : ")

print(listaNueva[:3]) #Esta salida solo se encarga de limitar el final sin tomarlo
#Imprime a Alexis, Sergio y Napy pero no a Nayomi

print("\nSalida desde con un parametro de inicio pero no de final : ")
print(listaNueva[1:]) #Esta imprime desde el indice 1 sin tomarlo hasta el indice final
#imprime a Sergio,Napy y Nayomi

print("\nRemplazar Dato de la lista : ")
listaNueva[0] = "Alexis Amadeus"
listaNueva[1] = "Sergio Numael" #Se especifica el indice con la lista y se ingresa el nuevo dato
print(listaNueva)
print("\nImprimir con for (Iterar): \n")

for nombre in listaNueva:
    print(f"El parce {nombre}")
else:
    print("\nYa no existen más nombres en la lista :( ")

