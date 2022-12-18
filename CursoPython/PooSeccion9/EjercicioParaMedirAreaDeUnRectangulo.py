print("Para el desarrollo de un ejercicio de pedida de datos para concoer el area de un rectangulo")

class Rectangulo:
    def __init__(this,base:int,altura:int):
        this.baseR = base
        this.alturaR = altura

    def Calcular_Area(this):
        return this.baseR * this.alturaR

rectan1=Rectangulo(4,5)
rectan2=Rectangulo(4,20)

print(rectan1.Calcular_Area())
print(rectan2.Calcular_Area())



