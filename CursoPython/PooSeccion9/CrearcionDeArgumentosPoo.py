class Persona:
                #Para declarar mas atributos de entrada en el contructor, es necesario establecer la entrada
                #dentro de los corchetes

    def __init__(self,nombre:str,apellido:str,edad:int):
        self.nombre = nombre
        self.apellido = apellido #Atributos de instancia de la clase para la declaracion de la clase Persona 
        self.edad = edad


persona1 = Persona('Sergio','Linares',22)
persona2 = Persona('Alexis','Linares',27)
persona3 = Persona('Jhamel','Ramos',25)

                                   #Es encesario que el atributo este definido en la clase porque asi no funciona en la entradaq de datos
print(f"Persona uno es : {persona1.nombre}")
print(f"Persona uno es : {persona2.nombre}")
print(f"Persona uno es : {persona3.nombre}")
