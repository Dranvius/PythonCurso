print("Conversion de temperaturas : ")

te= float(input("Cuál es la temperatura : "))

def cambioYDefinicionDeTemperatura (valorInicial, op = 0, tipo="Default" ):
    if op == 0:

        #Definicion inicial de grado
        tip = int(input("Cuál es el tipo de la temperatura celsius = 1 o fahrenheit = 0\n"))
        while tip == 1 and tip == 0:
            print(f"Valor incorrecto : {tip}")
            tip = int(input("Cuál es el tipo de la temperatura celsius = 1 o fahrenheit = 0\n"))

        #Definición de grado
        if tip == 1:
            estado = "CELSIUS"
        else:
            estado = "fahrenheit"

        #Si desea cambiar de temperatura
        op = int(input("¿ Desea Cambiar el el tipo de temperatura ? (Si = 1 y No = 0) : \n"))

        while op == 1  and op == 0:
            print(f"Valor incorrecto : {op}")
            op = int(input("¿ Desea Cambiar el el tipo de temperatura ? (Y = Si y N = No) : \n"))
        #Si desea cambiar la temperatura entrada a recursividad.
        if op == 1:
            cambioYDefinicionDeTemperatura(te, op, tip)
        else:
            print(f"Usuario no desea cambiar la temperatura."
                  f"\nSu Temperatura es : {valorInicial} - {estado}")
                                            #El valor inicila no esta definido X Si lo esta ya viene definido en la funcion los parametros de entrada de la funcion por default son los que definen el parametro incial pero necesita los otros
    elif op == 1:
        if tipo == "CELSIUS":
            valorInicial *= 2
            tipo = "Fahrenheit"
            print(f"La conversión de Celsius a Fahrenheit :\nValor = {valorInicial} - {tipo}")
        else:
            valorInicial /= 2
            tipo = "Fahrenheit"
            print(f"La conversion de Fahrenheit a Celsius :\nValor = {valorInicial} - {tipo}")



cambioYDefinicionDeTemperatura(te)