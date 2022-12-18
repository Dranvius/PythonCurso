#Otros datos de la tupla

print("Con esta funcion nosotros podemos iterar datos diferentes a la tupla y diccionario")

def iteracionListasOobjetosIterables(iterable):
    for  valor in iterable:
        print(valor)

#Iteracion con Str
print("Con Str : ")
iteracionListasOobjetosIterables('Hola')
print("--------------------------")
print("Con lista : ")
lista = ['Alexis','Sebastian','Sergio']
iteracionListasOobjetosIterables(lista)
print("--------------------------")
print("Con Tupla : ")
iteracionListasOobjetosIterables((1,2,3,4,5))
