print("Sistema de calificaciones ")

nota:int = int(input(" ¿Cuál es su nota? :"))

print("Los estandares de calificación son los siguientes ")
print("Si la calificación esta entre 9 - 10 es A")
print("Si la calificación esta entre 8 y menor a 9 es B")
print("Si está entre 7 y menor a 8: imprimir una C")
print("Si está entre 6 y menor a 7: imprimir una D")
print("Si está entre 0 y menor a 6: imprimir una F")

print("Cualquier otro valor no se parametriza")

if nota >= 9 and nota <= 10:
    print("Su nota es A")
elif 8 <= nota < 9:
    print("Su nota es B")
elif 7 <= nota < 8:
    print("Su nota es C")
elif 6 <= nota < 7:
    print("Su nota es D")
elif 0 <= nota < 6:
    print("Su nota es F")
else:
    print(f"Valor erroneo no asigando {nota}")