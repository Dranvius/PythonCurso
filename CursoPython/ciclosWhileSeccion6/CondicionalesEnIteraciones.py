print("Por medio de los ciclos es posible realizar realizar condiciones a a una iteración de datos")

stringCadena = "Hola Alexis"
conteo = 0
#Deseo saber cuantas A existen en esa cadena de string
#Aplicamos una condicion a cada recorrido del string (Es posible realizarlos con listas)

for letra in stringCadena:
    if letra == 'a' or letra == 'A':
        conteo += 1
else:
    print("Fin del ciclo")
    print(f"Numero de letras A en la oración {conteo}")
