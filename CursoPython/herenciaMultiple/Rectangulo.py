from Padre1HerenciaMultiple import FiguraGeometrica as fig
from Padre2HerenciaMultiple import Color as col

class Rectangulo(fig,col):
    def __init__(this,alto,ancho,color):
        fig.__init__(this,alto,ancho)
        col.__init__(this,color)


    def area(this):
        a = this.ancho * this.alto
        return a

    #Transmutación de la clase pero trae una funcion con el parametro Super().__str__()
    def __str__(this):
        return f"{super().__str__()} \nColor : {this.color} \nArea : {this.area()}"


