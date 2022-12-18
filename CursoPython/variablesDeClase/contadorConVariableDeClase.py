#El objetivo de este ejercicio es mostrar un paramero de incremento por cada objeto creado
#podemos establecer otros parametros que nos permitan mutar y evolucionar el compotamiento en poo
#por medio de esta sentencia.

class Persona():
    #Variable de clase para el incremento
    conteo = 0

    def __init__(this, name, lastName):
        Persona.conteo += 1 # Incrementa por cada registro se esta realizando un uso de variables de clase
                            # Con poo tambien se puede hacer con metodos de clase
        this.conteo = Persona.conteo
        this.name = name
        this.lastName = lastName

    def __str__(this):
        return  f"[ID : {this.conteo} \nNombre: {this.name}\nApellido: {this.lastName}]"



persona1 = Persona("Sergio","Linares")
persona2 = Persona("Alexis","Linares")
persona3 = Persona("Edward","Linares")

print(persona1)
print(persona2)
print(persona3)