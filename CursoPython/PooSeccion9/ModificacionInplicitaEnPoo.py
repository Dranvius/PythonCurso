print("Es posible modificar atributos ya estados en creados en Poo ")

class Persona:
    def __init__(self,Nombre:str,Apellido:str):
        self.name = Nombre
        self.ape = Apellido


persona1 = Persona("Sergio","Linares")

print(persona1.name)

persona1.name = "Edward" #Ojo con este proceso se puede cambiar los datos de la clase o atributo pero no es lo recomendadao por buenas practicas

print(persona1.name)