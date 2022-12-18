from ClaseAbstractaPadre import figuraAbstracta

class Cuadrado(figuraAbstracta):
    def __init__(this,alto,ancho):
        figuraAbstracta.__init__(this,alto,ancho)


#El metodo abstracto heredado de la clase padre es necesario y debe estar siempre implicito en la
    #Estructura (Esta clase es abstracta y sin este metodo no funciona más)
    def area_figura(this):
        return this.ancho * this.ancho


cuadrado1 = Cuadrado(10,10)

print(cuadrado1.area_figura())
