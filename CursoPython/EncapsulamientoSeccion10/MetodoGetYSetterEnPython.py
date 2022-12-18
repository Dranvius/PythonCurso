print("Se desea desarrollar una clase con las buenas practicas de Poo pero en python"
      "Utilizando el  metodo Setter y Gtter para atraer información")


class ClaseNormal:

    def __init__(this,nombre,apellido):
        this.__name = nombre
        this.__ape = apellido
    #-----------------------------------Getter-----------------------------------------------------
    # Utilizado para simplificar la instancia de llamado de de la funcion osea no necesita el ()
    @property
    def name(this):
        print("Llamando metodo Get")
        return this.__name

    @property
    def ape(this):
        print("Llamado metodo Get Apellido")
        return this.__ape

    #------------------------------------Setter-------------------------------------------------
    # Establece la instrucción de parametro setter
    # Valor recibido por el constructor
    @name.setter
    def name(this,nombre):
        print("Llamando metodo Set Nombre")
        this.__name = nombre

    @ape.setter
    def ape(this,apellido):
        this.__ape = apellido

persona1 = ClaseNormal("Alexis","Linares")

#Declaración Get------------------------------------------------------------------------- Primera Llamada Ge
print(persona1.name)
print(persona1.ape)
#Declaración Set------------------------------------------------------------------------- Mutación datos Set
persona1.name = 'Sergio'
persona1.ape = 'Ducuara'
#Imprimir salida rapida------------------------------------------------------------------ Llamada Get
print(persona1.name)
print(persona1.ape)





