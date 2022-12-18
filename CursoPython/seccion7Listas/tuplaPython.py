print("EL uso de tuplas es algo parecido al de listas pero las tuplas no pueden cambiar ni borrarse")

tuple0 = ('Alexis','Sergio','Nayomi')
tuple2 = ('Sergio',) #Las tuplas deben de tener una coma al final solo si se declara un solo valor
#Es posible imprimir
print(tuple0)
#Es posible conocer su longitud
print(len(tuple0))
#Es posible acceder a un indice en la tupla
print(tuple0[0])
#Es posible imprimir por rangos
print(tuple0[0:2])
#Es posible concatenar con un for
for nombre in tuple0:
    print(nombre, end= ' ') #Forma de inprimir
#Para modificar es necesario transformar la tupla a una lista
print("\nModificación de tupla por medio de trasnmutación de tipo")
newLista = list(tuple0) #Conversión de tupla a lista
newLista.append("Napy") #Agregar y modificación de la lista/Tupla
tuple0 = tuple(newLista) #Conversion de lista a tupla  (Es importante para su remplazo)
print(f"Nueva tupla : {tuple0}")
#Para borrar una tupla utilizamos la funcion del
del tupla0
print(tupla0)

