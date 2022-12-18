num: int = int(input("Ingrese un número 1 - 3 : "))
textNum:str = ''

if num == 1:
    textNum = 'Uno'
elif num == 2:
    textNum ='Dos'
elif num == 3:
    textNum = 'Tres'
else:
    textNum = ''


#Control de excepciones con If
if textNum == '':
    print(f"Error valor incorrecto : {num}")
else:
    print(f"\nValor : {num}\nTexto : {textNum}")
