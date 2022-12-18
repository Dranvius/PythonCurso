#from PooParametroDeSoloLecturaInmutableSinSetter import NuevaClase2
from ClasePadrePersona import Persona   #Modularidad En programación Py
print("Esta clase Hereda atributos y funciones de la clase padre")

class Empleado(Persona): #Herencia de la clase
    def __init__(this,nombre,apellido,salario):
        super().__init__(nombre,apellido) #Uso de atributos de la clase padre
        this.sala = salario

persona1 = Empleado('Sergio','Linares','3000000')


persona1.salida_Basica()
