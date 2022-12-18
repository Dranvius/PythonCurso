print("Vamos a utilizar la poo para desarrollar nuevas caracteristicas de entrada de datos ")

class NuevaClase:
    def __init__(this,door1,door2):
        this.entrada1 = door1
        this.entrada2 = door2

    def salida_por_Panatalla(this):
        print(f"Salida por pantalla basica de datos : \n{this.entrada1}\n{this.entrada2} ")


nueva1=NuevaClase("Entrada1","Entrada2")
nueva1.telefono = 123456789 #Se pueden establecer atributos de manera dinamica al ya ser establecida la clase.
nueva1.salida_por_Panatalla()

print(nueva1.telefono)