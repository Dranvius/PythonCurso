print("Se desarrolla un juego de football del hijo de Eduardo,"
      "Él debe pedir permiso a su jefe para ir"
      "a ver el partido de su hijo")

print("\n Solución \n")

#Pedir permiso:
#Para pedir permiso
# -Eduardo debe tener 500 dias de trabajo
# -y llevarle un tinto a su jefe (El tindo debe estar caliente o si no F)

diasT = int(input("Cuantos Días trabajaste Eduardo : "))
cafe = int(input("Quieres llevarle un cafe a su jefe (1 = si o 0 = no ) : "))
permiso: bool = False
calentar = int(input("Desea calentar el cafe 1 = si y 0 = no : "))


#Calentar cafe
if cafe == 1 and calentar == 1 :
    print("Educardo calento el cafe")
    cafe = True #Cafe caliente
elif calentar != 1 or cafe != 1:
    print("No desea calentar el cafe")
elif cafe != 1 or calentar != 1:
    print("No lleva tiene cafe")

#Pedir permiso
if diasT >= 500 and cafe == True:
    print("Eduardo tiene el permiso")
else:
    print("Eduardo  no tiene el permiso del jefe ")