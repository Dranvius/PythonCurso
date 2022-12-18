#Se instancian las variables por medio de modularidad  y traen las  funciones correspondientes.
from Padre1HerenciaMultiple import FiguraGeometrica
     #Documento                    #Clase
from Padre2HerenciaMultiple import Color


class Cuadrado(FiguraGeometrica,Color):
    def __init__(this,color,ancho): #Constructor para la calse Cuadrado

        FiguraGeometrica.__init__(this,ancho,alto = 0) #Parametro de entrada por default cuando no es necesaria una variable(alto = 0)
        Color.__init__(this,color)


    def area(this):
        a = this.ancho * this.ancho
        return a


    #Sobre Escritura de funciones Str de la padre
    #Se traen los valores de  la propia clase y no de la clase padre pero se puede traer metodos en de sobre escritura
    #de metodos.
    def __str__(this):
        return f"Lado 1 : {this.ancho}\nLado 2 : {this.ancho}\nColor : {this.color}\nArea : {this.area()}"


