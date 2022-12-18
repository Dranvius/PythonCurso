
class vehiculo:
    def __init__(this,velocidad,llantas,color,pasajerosPermitidos):
        this.__velocidad = velocidad
        this.__llantas = llantas
        this.__color = color
        this.__pasajeros = pasajerosPermitidos

#Velocidad-----------------------------------------
    @property
    def velocidad(this):
        return this.__velocidad
    @velocidad.setter
    def velocidad(this, valorNuevo):
        this.__velocidad = valorNuevo
#Llantas--------------------------------------------
    @property
    def llantas(this):
        return this.__llantas
    @llantas.setter
    def llantas(this, nuevoValorLLantas):
        this.__llantas = nuevoValorLLantas
#color----------------------------------------------
    @property
    def color(this):
        return this.__color
    @color.setter
    def color(this, nuevoColor):
        this.__color = nuevoColor
#pasajeros--------------------------------------
    @property
    def pasajeros(this):
        return this.__pasajeros
    @pasajeros.setter
    def pasajeros(this, nuevaCantidadDePsajeros):
        this.__pasajeros = nuevaCantidadDePsajeros


    #FUNCIONALIDAD

    def __str__(this):
        return f'Velocidad : {this.__velocidad} ' \
               f'Pasajeros : {this.__pasajeros} ' \
               f'Color : {this.__color} ' \
               f'Llantas : {this.__llantas} '


    def velocidad(this):

        if(this.__velocidad > 300):
            print("So fast Dude, bajale mi rey")
        else:
            print("Ur my bitch")