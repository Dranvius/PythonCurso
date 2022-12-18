print("Por medio de funciones especial nosotros podemos realizar mutaciones de datos ")
print("Ejemplo : ")

print("Declaramos variables ")

variableStringParaMutarAInt1: str = "1"
variableStringParaMutarAInt2: str = "2"
variableStringParaMutarAFloat: str = "1.2020"

print("De String a Int:")
print("*Antes de la modificación:*")
print(f"Dato : {variableStringParaMutarAInt1}\nTipo De Dato: {type(variableStringParaMutarAInt1)}")
print("*Despues de la modificación:*")
print(f"Dato: {int(variableStringParaMutarAInt1)}\nTipo De Dato {type(int(variableStringParaMutarAInt1))}")
print("*-------------------------*")
print("De String a Float:")
print("*Antes de la modificación:*")
print(f"Dato : {variableStringParaMutarAFloat}\nTipo De Dato: {type(variableStringParaMutarAFloat)}")
print("*Despues de la modificación:*")
print(f"Dato: {float(variableStringParaMutarAFloat)}\nTipo De Dato {type(float(variableStringParaMutarAFloat))}")
