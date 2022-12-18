print("Agregar ")

#Agregar otro indice a la lista
listaNueva = ["carlos","Felipe","Carmen","Hector"]

print(listaNueva)

#Funcion para agreagr lista
print("\nAgregar Lista funcion append()\n")
listaNueva.append("Sergio")
listaNueva.append("Alexis")
listaNueva.append("Samira")
print(listaNueva)

print("\nIngresar desde indice\n")

listaNueva.insert(1,"agregar con indice")
#Funcion que agrega desde el indice escogido (No borra el indice actual solo crea uno nuevo desde  el indice 1 para adelante)
#El indice uno no se modifica, solo todos todos aumentan un dince para la nueva entrada en la lista pero no modifica el indice

#Remover un elemnto
print("Remover el valor por valor mas no por indice funcione remove()")
listaNueva.remove("Sergio") #Se remueve a Sergio por medio de su nombre exacto en la ista
#Remover el ultimo elemento
print("Remover el ultimo elemnto de la lista funcion pop()")
listaNueva.pop()
#Remover elemnto desde un indice indicado
print("Se desea eliminar un elemento desde un indice indicado con el comando del (del nombreLista[indice])")
del listaNueva[0] #Elmina el primer varlor de la lista (Puede ser cualquier indice)
#Eliminar todo los emlemntos de la lista
print("Para eliminar todos los elementos de la lista utilizamos la funcion : clear() ")
listaNueva.clear() #Elimina todos los valores de la lista
#Eliminar la lista de memoria utilizamos la funcion Del pero con el nombre de la lista y bo cobn el indice
del listaNueva
print(listaNueva)
