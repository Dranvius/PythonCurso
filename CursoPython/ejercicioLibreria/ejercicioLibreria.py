
print("Ejercicio Libreria\n")

#Pedida de datos-----------
nombreLibro:str = input("¿ Cuál es el nombre del libro ? :")
idLibro: int = int(input("Ingrese el ID del libro : "))

while idLibro <= 0:  # Mientras la condición sea verdadera se repetira el buble
    idLibro: int = int(input("Ingrese el ID del libro : "))

precioLibro: float = float(input("¿ Cuál es el precio del libro ? : "))

while precioLibro <= 0:  # Mientras la condición sea verdadera se repetira el buble
    precioLibro: float = float(input("¿ Cuál es el precio del libro ? : "))

envioGratuito: bool = bool(input("¿El envio fue gratuito : ? (True = Si y False = No) : "))

#Falta rematar este codigo
if envioGratuito == True:
    envioGratuito = "Gratis"
elif envioGratuito == False:
    envioGratuito ="No es Gratis"

else:
    print("Valor incorrecto")
#salida datos

print(f"El nombre del libro es {nombreLibro}\nID : {idLibro}\nPrecio : {precioLibro}\nEl envio {envioGratuito}")
