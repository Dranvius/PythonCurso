#Declaracion de clases, atributos y construcor en python

class Persona:
    def __init__(self): #Conn esta referncia Self se estan escribiendo datos por default para el uso de atributos
        self.nombre ='Sergio' #Declaración de Atributos de la clase
        self.apellido = 'Linares' #Declaracion de otro atributo de la clase
        self.edad = 22 #Declaracion de edad

    #pass Se usa esta funcion para declarar el uso de una funcion vacia sin parametro


print(Persona().edad)