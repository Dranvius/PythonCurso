print("Calculadora de inpuestos de un pago")

valorTotal = int(input("Cuál es el valor total de la compra : "))

def pagoConInpuestos(valor):
    iva = 0.019
    inpuestoAoB = valor >= 2000000

    if inpuestoAoB == True:
        inpValoresAltos = 50000
        iva = valor * iva

        return int(valor + inpValoresAltos + iva)

    elif inpuestoAoB == False:                        #Condicional Muy marcada Posible simplificación
        inpValoresBajos = 25000
        iva = valor * iva

        return int(valor + inpValoresBajos + iva)


print(pagoConInpuestos(valorTotal))