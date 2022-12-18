print("La con concatenación es simplemente el llamado de variables para la ejecuón de salida por consola")
print("Declaración de variables e impresión con tipode de datos String")
print("Ejemplo:")

miName: str = "Sergio "+" Linares "+" Ducuara" #Observe la concatenación por medio de Strings y +

print("Concatenación 1--------- Con F") #Concatenación con F (Super recomendado)

print(f"-My name is : {miName}  \n-Tipo de dato:  {type(miName)}")

print("Concatenación 2---------- Con +") #Concatenación con + (No recomendado)

print(f"-Mi nombre es :" + miName + "\nProceso")
print(f"-Tipo de dato : {type(miName)}")

print("Concatenación 3----------Con comas") #Concatenación con comas (Recomendado)

print ("Mi nombre es:", miName ,"Tipo de dato", type(miName))