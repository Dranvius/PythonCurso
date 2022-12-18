from abc import ABC, abstractmethod
            #Importamos ABC que es la clase abstracta y el decorador abstractmenthod


class figuraAbstracta(ABC):
    def __init__(this,alto,ancho):
        this._alto = alto
        this._ancho = ancho


#Todas las clases que hereden de esta clase padre tendran que determinar si o si sus metodos abstractos
    #Además la clase que herda se convertira abstracta.
    #Esto es utilizado para determinar patrones necesarios o caracteristicas necesarias en cada funcion.

#Definición de clase abstracta
    @abstractmethod
    def area_figura(this):
        pass
    #Determinamos la funcion pero al existir varación entre clases (Triangulo,Cuadrado).
    #No determinamos ningun proceso.
    #Se le agrega el proceso en la sobrescrición de metodos.

    #Getter-------------------------------------------
    @property
    def alto(this):
        return this._alto

    @property
    def ancho(this):
        return this._ancho

    #Setter--------------------------------------------
    @alto.setter
    def alto(this,newValue):
        this._alto = newValue

    @ancho.setter
    def ancho(this,newValue):
        this._ancho = newValue
