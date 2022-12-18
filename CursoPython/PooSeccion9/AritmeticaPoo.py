print("Desarrollo de ejrcicio utilizando POO y sin modularidad ")

class operation:
    def __init__(this,num1,num2):
        this.numero1 = num1
        this.numero2 = num2
    """""
    Hola eso es un comentario parce Ome 
    """""

    def Suma(this):
        return this.numero1 + this.numero2

    def Resta(this):
        return this.numero1 - this.numero2

    def Multi(this):
        return this.numero1 * this.numero2

    def Divici(this):
        return this.numero1 / this.numero2

    def exponente(this):
        return this.numero1 ** this.numero2


par1=operation(4,5)

print(par1.Suma())
print(par1.Resta())
print(par1.Multi())
print(par1.Divici())
print(par1.exponente())



