#Funcion que recibe como parametro un diccionario

def iteracionDiccionario(**dic):#Iteracion con items
    for clave, valor in dic.items():
        print(f'Clave : {clave}\nValor: {valor}')

iteracionDiccionario(Huevos = 6, Carne = 2, gaseosa = 2, arroz = 4)