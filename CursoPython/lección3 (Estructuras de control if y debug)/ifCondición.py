print("Uso de condicionales  ")

variable1: str = 'hola'
varaible2: bool = True


#Con solo una variabled str
#Nule = False
# != Nule = True 
if variable1:
    print("Si la variable no esta vacia, devuelve un True")
else:
    print("Si la variable esta vacia devuelve un False")


if variable2 and True:
    print("Si es True va por este camino")
elif variable2 == 1:
    print("Podemos capturar condiciones al no pasar una condición")
else:
    print("Cuando todo no sea verdad viene acá")

