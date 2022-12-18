print("Ejercicio De Perimetro y area de un rectangulo\n")

print("Solicitamos Datos\n")

ancho = int(input("Ingrese el ancho del Rectangulo"))
alto = int(input("Ingrese el alto del rectangulo"))

# Operación para saber cuál es el perimetro y area

area = ancho * alto
perime = (ancho + alto) * 2  # Siempre exite una forma diferente de llegar a una solución
perime2 = ancho * 2 + alto * 2  # Siempre exite una forma diferente de llegar a una solución

print(f"El area del  rectangulo es : {area}")
print(f"El perime : {perime}")
print(f"Segunda formula de perimetro : {perime2}")
