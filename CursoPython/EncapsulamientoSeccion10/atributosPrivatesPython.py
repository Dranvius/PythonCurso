print("Privatización de atributos ")

class privateClass:

    def __init__(this,atributo1,atributo2):
        this.__atri1 = atributo1
        this.__atri2 = atributo2


persona1 = privateClass('Sergio','Linares')

#persona1.
#No puedo llamar el atributo porque esta en privado

