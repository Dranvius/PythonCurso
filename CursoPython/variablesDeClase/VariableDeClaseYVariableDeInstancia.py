class NameGenerico():

    variableDeClase = 'My name is Sergio' #Variable de instancia

    def __init__(this,variableDeInstancia):
        this.variableDeClase = variableDeInstancia

persona1 = NameGenerico("Hello")    # La variable de instancia varia dependiendo de la instancia realizada.
print(NameGenerico.variableDeClase) # Esta variable permite acceder desde cualquier clase sin iportar que.


