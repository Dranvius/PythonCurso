print("Por medio de Poo se desea conocer el volumen de un cubo ancho * altura * profundidad")

class Cubo:
    def __init__(this,ancho,altura,profundidad):
        this.anchoC = ancho
        this.profundidadC = profundidad
        this.alturaC = altura

    def Volumen_Cubo(this):
        return this.anchoC * this.alturaC * this.profundidadC


cubo1 = Cubo(3,5,6)
print(cubo1.Volumen_Cubo())