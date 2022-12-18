print("En este archivo se busca establecer solo parametros que tengan como objetivo la inmutabilidad de los atributos de una clase"
      "Se quitan la función Setter")

#Clase de solo lectura de python

class NuevaClase2:
    def __init__(this,nombre):
        this.__name = nombre

    #Get Funciona para atraer el elemnto del constructor inicializado en el objeto
    @property
    def name(this):
        return this.__name

    #Setter lo utilizamos para mutar atributos del objeto instanciado
    #@name.setter
    #def name(this,nombre):
    #    this.__name = nombre


print("Sin el metodo Set no podemos cambiar el atributo del constructor pero si llamarlo ")

#Para realizar pruebas se debe estabelcer una condicion que solo parametrice el archivo de la casle o donde se ahce las pruebas

#Pruebas-----------------------------------------------------

if __name__ == "__main__":
    persona1 = NuevaClase2("Sergio")