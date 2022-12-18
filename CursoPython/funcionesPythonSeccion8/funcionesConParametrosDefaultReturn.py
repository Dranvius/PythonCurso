print("Es posbile utilizar funciones con parametros default que determinan una opción si no se le ingresan los parametros")

print("Declaramos la funcion")



#Funcion 1 : (parametors default con un return general o funcion VOID)
def nuevaFuncion(num1 = 0, num2= 0):
    return num1 + num2

    # Se declaran parametros default en el caso de que no se ingresen datos para el uso de la funcion
    # Return Esta linea de codigo se encarga de devolver datos de la función tambien conocido como dato NO VOID
    # Devuelve un entero

#Funcion 2 : (Funcion con parametro de entrada parametrizada)
def nuevaFuncion1(num1:int = 0, num2:int = 0) -> int:
    print(num1 + num2)

    #Devuelve un proceso
    #Se declaran parametros default en el caso de que no se ingresen datos para el uso de la funcion
    #Al declararse  una función es posible que sea Void
    #(Apesar que python use datos dinamicos para el uso de variables esto se ve reflejado en sus funciones pero podemos establecer
    #un pequeño deliniamiento del uso de tipo de variables)

print("Uso de las funciones")
print(f"Funcion no void (1): {nuevaFuncion(1,4)}")
nuevaFuncion1(1,6)