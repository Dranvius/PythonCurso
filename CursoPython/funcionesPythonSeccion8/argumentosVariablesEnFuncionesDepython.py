print("En python nosotros podemos tener como parametros varios datos; especificamente entradas tipo Tupla")
    #Argumentos Variables o Args
    #Nombre funcion / parametro de varios datos (importante recordar que lo toma como tupla)
def multipleValores(*numeros):
    for numero in numeros: #Iteración como si fuera una estructura de datos tipo tupla
        print(numero)
        #Operaciones de la funcion

#Llamada de función
multipleValores(1,2,3,4,5,6,7,8,9)
                #Ingreso de multiples datos