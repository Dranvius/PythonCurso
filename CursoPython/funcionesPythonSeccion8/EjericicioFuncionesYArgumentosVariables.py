print("Necesitamos realizar realizar la suma de todos los parametros de un parametro de argumentos varaibles")

#Suma de toda la tupla de argumentos varaibles con un parametro indice
def sumaDeParametrosVariados(*numeros,numeroSuma):
    for numero in numeros:
        print(numero + numeroSuma)

                        #Primer parametro Args / Segundo parametro numeroSuma

sumaDeParametrosVariados(1,2,3,4,5,6,7,8,9,10,numeroSuma = 2)

#Suma de todo el args
def sumaTodo(*args):
    numeroT: int = 0
    for numero in args:
        numeroT += numero
    return numeroT

print(f"\nLa suma de todos los argmentos varaibles es {sumaTodo(1,2,3,4,5,6,7,8,9,10)}")
