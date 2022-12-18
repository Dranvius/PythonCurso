print("Ejercicio para medir loos rangos de edad y una salida simple por consola ")

edad: int = int(input("¿Cuál es su edad? : "))

if edad > 0 and edad <= 10 :
    print(f"La infancia es increible :=) : {edad}")
elif edad > 10 and edad <= 20:
    print(f"Muchos cambios y muchos estudios : {edad}")
elif edad > 20 and  edad <= 30:
    print(f"Ya comienza el dark souls : {edad}")
elif edad > 30 and edad <= 50:
    print (f"Ya se le fue el Tren papi")
else:
    print("Edad incorrecta")
