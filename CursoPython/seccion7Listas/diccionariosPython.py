print("(Funciones principales)Los diccionarios son esttructuras de datos clave valor que permiten alamcenar datos y consultarlos por su clave"
      "-Estructura de datos clave valor"
      "-El indice puede ser cualquier dato"
      "-Las caratersiticas permiten organizar valores en capas dobles ")

#dict (Key, value)

diccionario = {
    #Llave      Valor
    'Alexis' : 'Economista',
    'Sergio' : 'Desarrollador',
    'Jhamel' : 'Arquitecto'
}

print(diccionario)

#Conocer el largo del diccionario
print("\nLargo del diccionario : ")
print(len(diccionario))
#Acceder a un valor en particular (Key)
print("\nTraer datos :")
print(diccionario['Sergio']) #Para acceder a un valor en especifico tenemos que determinar la key o llave
#Otra forma para recuperar un elemento
print("\nTraer datos :")
print(diccionario.get('Alexis'))
#Modificar elementos
print("\nModificar elemento")
diccionario['Sergio'] = 'Programador' #MODIFICA EL VALOR MÁS NO LA LLAVE
print(f"\n{diccionario}")
#Recorrer los elemntos (Solo valores)
print("Solo trae los elementos : ")
for termino in diccionario:
    print(termino)
else:
    print("No hay más elementos en el diccionario")

#Recorrer los elemntos (Solo valores)
print("\nTrae Clave y valor por medio de los dos terminos : ")
for termino, valor in diccionario.items(): #Items tiene la funcion de devolver los terminos separados por termino y valor (Itera con llave y valor)
    print(f"\nKey : {termino} \nValor : {valor}")
else:
    print("\nNo hay más elementos en el diccionario ")

#Reccorrer diccionario solo para tener las llaves
print("LLaves For : ")
for llave in diccionario.keys(): #Keys() Funciona para que en el for solo itere el Keys
    print(llave)
#Reccorre el dicionario pero solo obtiene los valores
print("Valores For:")
for valor in diccionario.values():
    print(valores)
#Comprobar si existe algun elemnto en el diccionario
print("Existencia de algun elemento en el diccionario (Sergio esta en el diccionario(LLave))")
print('Sergio' in diccionario)
#Agregar un dato al diccionario
print("Agregar un elemento : por medio de clave y valor")
diccionario['nuevoElemento(Llave)'] = 'Valor de la llave'
print(diccionario)
#Remover un elemento funcion .POP()
print("Remover el valor y clave Sergio")
diccionario.pop('Sergio')
#Borrar todo el diccionario
print("Borrar todo el diccionario pero deja la variable")
diccionario.clear()
print(diccionario)
#Eliminar hasta la varaible
del diccionario
print(diccionario)





