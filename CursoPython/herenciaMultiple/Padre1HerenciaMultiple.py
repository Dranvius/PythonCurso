#Para que no xista el problema de caractersticas de sobrecarga de funcionalidad recursiva se debe privatizar variables
#OJO CON PATRONES DE DISEÑOS CON DIFEENTES CONTEXTOS
class FiguraGeometrica:

    def __init__(this,ancho,alto):
        if this.valores_Correctos(alto):               #Valores dentro del rango
            this._alto = alto
        else:                                               #(Establecemos valores que delimitan en POO)
            this._ancho = 0
            print(f"Valor erroneo : {alto}")
        if this.valores_Correctos(ancho):              #Valores dentro del rango
            this._ancho = ancho
        else:
            this._alto = 0
            print(f"Valor erroneo : {ancho}")


#----------------------------------------------------------

    def __str__(this):
        return f"Ancho : {this._ancho} \nAlto : {this._alto}"


#-------------------------------------Getter y Setter Ancho
    @property
    def ancho(this):
        return this._ancho

    @ancho.setter
    def ancho(this,anchoNew):
        if this.valores_Correctos(anchoNew):
            this._ancho = anchoNew
        else:
            print(f"Valores erroneo : {anchoNew} ")

#----------------------------------------Getter y setter Alto

    @property
    def alto(this):
        return this._alto

    @alto.setter
    def alto(this,newAlto):
        if this.valores_Correctos(newAlto):
            this._alto = newAlto
        else:
            print(f"Valores erroneo : {newAlto} ")


    def valores_Correctos(this,valor):          #Determinamos una funcion para determinar los datos de entrada en el
                                                #De la funcion, en este caso se esta determinando los valores de un rang
                                                #de 0 a 10
        return True if 0 <valor< 10 else False