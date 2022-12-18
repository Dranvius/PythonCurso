from vehiculoEjercicioHeranciaPadre import vehiculo

class Carro(vehiculo):

    def __init__(this,tamaño,modelo,velocidad,llantas,color,pasajerosPermitidos):
        super().__init__(velocidad,llantas,color,pasajerosPermitidos)
        this.tamaño = tamaño
        this.modelo = modelo


    #------------------------------------------
    @property
    def tamaño(this):
        return this.__tamaño
    @tamaño.setter
    def tamaño(this,newTamaño):
        this.__tamaño = newTamaño

    #------------------------------------------
    @property
    def modelo(this):
        return this.__tamaño
    @modelo.setter
    def modelo(this,nuevaVariacón):
        this.__tamaño = nuevaVariacón


    def __str__(this):
        return  f"{super().__str__()} " \
                f"Tipo : {this.tamaño} " \
                f"Modelo : {this.modelo}"

carro1 = Carro("Big","New",400,4,'negro',4)

print(carro1)
