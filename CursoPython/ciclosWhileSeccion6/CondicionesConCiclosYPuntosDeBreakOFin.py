print("Este pequeño codigo explicara como se utiliza la linea de codigo break.")

#Ejercicio solo para buscar UNA letra entre la cadena de String

cadenaString:str = input("Inserte un texto : ")
veces:int = 0

for letra in cadenaString:
    if letra == 'b' or letra == 'B':
        print("Esta es la primera B")
        print(f"\nNúmero de veces repetidas: {veces}")
        break
    elif cadenaString[-1] == letra and len(cadenaString) == veces: # Es mejor salir por rango final y varaible final
        print("No existe letras B en la palabra")
    else:
        veces += 1

else:
    print("Con el funcion break el codigo no llega hasta acá solo cuando no se encuentra ninguna palabra B")