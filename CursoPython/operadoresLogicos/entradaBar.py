print("En un bar existen condiciones para beber entrar, tomar cerveza y si es mujer vale madres entra")
print("Necesario ser mayor de 18 y para beber cerveza necesario ser mayor de 21 años")

print("Pedida De Datos")

edad = int (input("Cuál es su edad, Ome ? "))
sexo = int (input("Cuál su genero (1 = mujer y 0 = hombre)"))

#Entrada Bar
if (edad >= 18 or sexo == 1) and edad > 15:
    print("Entraste al bar :) ")
    if(edad >= 21):
        print("Puedes Beber")
    else:
        print("No puedes beber ")
else:
    print("¡Largo!")

print("*---------------------------*")

#print("-Para entrar en la zona VIP es necesario estar en un rango de edad entre los 25 - 30 años asi pailas mi socio-")

#Entrada VIP

print("--Para ingresar debes tener un rango de edad especial---\n")

if edad >= 25 and edad <=30:
    print("*Entraste al VIP* :)")
else:
    print("*No puede entrar* :(")