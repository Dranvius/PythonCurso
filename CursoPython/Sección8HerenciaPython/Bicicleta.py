from vehiculoEjercicioHeranciaPadre import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(this, tamaño,tipo,velocidad,llantas,color,pasajerosPermitidos):
        super().__init__(velocidad,llantas,color,pasajerosPermitidos)
        this.tamaño = tamaño
        this.tipo = tipo


    #----------------------------------------------------
    @property
    def tamaño(this):
        return this.tamaño
    @tamaño.setter
    def tamaño(this,tamañoNuevo):
        this.tamaño = tamañoNuevo
    #------------------------------------------------------
    @property
    def tipo(this):
        return this.tipo
    @tipo.setter
    def tipo(this,nuevoDato):
        this.nuevoDato


