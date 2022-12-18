print("Se desea saber en cuál estación del año se ecnuentra en función de un mes")

mes = int(input("¿ En qué mes se encuentra ? : "))

if mes >= 3 and  mes <= 5:
    print(f"Primavera: {mes}")
elif mes >=6 and mes <= 9:
    print(f"Verano: {mes}")
elif mes>=10 and mes<=11:
    print(f"Otoño: {mes}")
elif mes == 12 or mes < 2 and mes > 0:
    print(f"Invierno: {mes}")
else:
    print(f"Valor incorrecto {mes}")