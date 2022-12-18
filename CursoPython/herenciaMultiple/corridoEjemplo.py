from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado('Azul',-1)
print("Cuadarado 1".center(50,'-'))
print(cuadrado1)
print("Cuadarado 2".center(50,'-'))
cuadrado1.ancho = 4
print(cuadrado1)
print("Rectangulo 1".center(50,'-'))

rectangulo1 = Rectangulo(1,5,"Blue")
print(rectangulo1)