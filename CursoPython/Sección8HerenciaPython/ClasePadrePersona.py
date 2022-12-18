print("La explicación de herencia hace referencia al apropiamiento de atributos y funciones de una clase en especial"
      "Existe una clase Padre que hereda a otra clase sus atributos y funciones con el fin de adaptar la clase a una necesidad especifica")

#CLASE PADRE
class Persona:
    def __init__(this,nombre,apellido):
        this.__name = nombre
        this.__lastName = apellido

    #Getter-------------------------------------------------

    #Name
    @property
    def name(this):
        return this.__name

    #lastName
    @property
    def last_Name(this):
        return this.__lastName

    #Setter-------------------------------------------------

    #name
    @name.setter
    def name(this,nombre):
        this.__name = nombre

    #LastName
    @last_Name.setter
    def last_Name(this,apellido):
        this.__lastName = apellido


    def salida_Basica(this):
        print(f"Hola mi nombres es {this.__name} {this.__lastName}")


#SobreEscritura metodo STR salida por pantalla basica-----------------------------------------
    def __str__(this):
        return f'Nombre : {this.__name} Apellido : {this.__lastName}'

persona1 = Persona('Sergio','Linares')

persona1.salida_Basica()