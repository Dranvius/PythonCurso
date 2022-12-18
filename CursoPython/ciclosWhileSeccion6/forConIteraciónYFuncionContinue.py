print("Algoritmo con iteración range y continue")

for num in range(10):
    if num % 2 == 0:
        print(f"Numero par {num}")
    else:
        print(f"No es numero par {num}")

#Ejemplo 2 Con el blocke continue; esta funcion termina la operacion y continua con el siguiente blocke de codigo
print("\n")
for num in range(6):
    if num % 2 != 0:
        continue #Salta al otro blocke de if se sale del if o continua iterando ver conportamiento con continue
        print("helloTest") #No inprime
    print(num)