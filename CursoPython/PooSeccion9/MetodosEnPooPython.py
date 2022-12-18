print ("Vmos a declarar metodos para el desarrollo de las clases")

class Metodos:
    def __init__(self,name,lastName):
        self.nombre = name
        self.apellido = lastName

        pass

    #Metodos en Poo con python
    def nueva_funcion_Salida_Por_Consola(self):
        print(f"El nombre es : {self.nombre}\nEl Apellido es : {self.apellido}")


persona1=Metodos("Sergio","Linares")
persona2=Metodos("Alexis","Linares")

persona1.nueva_funcion_Salida_Por_Consola()
persona2.nueva_funcion_Salida_Por_Consola()

