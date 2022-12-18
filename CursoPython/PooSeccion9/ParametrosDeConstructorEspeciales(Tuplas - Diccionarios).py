print("El desarrollo de un constructor utilizado para recibir tuplas y diccionarios ")

class EntardaTexto:
                     #Los parametros de entrada de tuplas y diccionarios son:
    def __init__(this,*tuple,**diccionario):
        this.tup = tuple
        this.dic = diccionario

    def salida_datos_estructuras(this):
        print("Tupla")
        for num in this.tup:        #Uso de tuplas para el POO
            print(num)
        print("Diccionario")
        for llave, valor in this.dic.items():     #Iteración con diccionarios
            print(f"La llave es : {llave} - El valor es : {valor}")
                        #Entrada de parametro   #Declaración de diccionario
entrada1 = EntardaTexto(tuple =(1,2,3,4,5), Sergio = 'Linares', Alexis = 'Ducuara')

entrada1.salida_datos_estructuras()