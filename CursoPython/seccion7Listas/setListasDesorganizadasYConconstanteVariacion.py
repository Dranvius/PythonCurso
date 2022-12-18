print("Las listas Set se caracterizan por variar constantemente en cada ejecución"
      "pero los datos almacenados en la lista set seguiran siendo los mismos"
      "-No admite elemntos duplicados en una lista de datos"
      "-No tiene indice porque varian"
      "-No puede Borrar datos que no se encuentren en la lista")

setList = {'Alexis','Sergio','Napy'}

#En cada impresion varian pero no con ciclos For
print(setList)
#Para conocer el largo de los elementos

print("Largo lista : ")
print(len(setList))

#Conocer si un elemento se encuentra en el Set
print("\nConocer si un elemnto se encuentra en la lista : ")
print("Alexis se encuentra en el set")
print('Alexis' in setList) #Devuelve un Booleano
#Agregar más elementos al Set
print("\nAgregar elemnetos al set")
setList.add('Nayomi')
print(setList)

#Eliminar elementos detallado por medio de su valor
print("Sergio fue eliminado")
setList.remove("Sergio")
print(setList)
#Eliminar valor del set en caso de que no se encuentre el elemento no lance error funcion discard(Elemento)
print("Alexis fue eliminado")
setList.discard("Alexis") #No lanza error en el anterior si lo hacia
print(setList)
#Elminar por completo
del setList
print(setList)



#El set no soporta elementos duplicados (Si quiere agregar a Alexis no me va a dejar)
