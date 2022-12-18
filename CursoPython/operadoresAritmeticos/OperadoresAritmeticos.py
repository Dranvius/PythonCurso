print ("Operadores Aritmeticos")

#Los operadores aritmeticos son utilizados para realizar operaciones entre numeros.

print("Ingresamos dos numeros")

num1 = int(input("Ingrese un numero : "))
num2 = int(input("Ingrese otro numero : "))

#Operaciones y sus cualidades
suma = num1 + num2
resta = num1 - num2
multiplicación = num1 * num2
divisi = num1 / num2
divsiónCerrada = num1 // num2
divisionModular = num1 % num2
pow = num1 ** num2
      #Base - Potenciador

print(f"Suma : {suma}")
print(f"Resta : {resta}")
print(f"Multiplicación : {multiplicación}")
print(f"División : {divisi}")
print(f"División (Redondeada) : {divsiónCerrada}")
print(f"División Modular (Residuo de la división) : {divisionModular}")
print(f"Potencia de numeros : {pow}")