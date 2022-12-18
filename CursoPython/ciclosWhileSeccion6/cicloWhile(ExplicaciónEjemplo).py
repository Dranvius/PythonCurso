#Si la condición es verdadera se repite y si la condición es falsa sale del bucle

#Ejemplo 1

num = int(input("Ingrese un numero, el número debe ser : 4 - "))

while num != 4: #Numero diferentes a 4, para salir del bucle se debe ingresar el 4
    print(f"Error el numero debe ser 4 y ingreso el {num} ")
    num = int(input("Ingrese un numero, el número debe ser : 4 - "))
else:
    print("Fin ciclo While")

print(f"El numero digitado es correcto {num}")

#Ejemplo 2 Conteo

conteo: int = 4
num2: int = 0
veces = 0

while num2 < conteo :
    num2 += 1
    veces += 1
    print(f"Veces repetidas {veces}")
else:
    print("Fin ciclo While")


