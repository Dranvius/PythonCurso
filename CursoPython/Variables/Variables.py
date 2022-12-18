"Las varaibles en python se caracterizan por ser Adaptables en función del dato que se desea almacenar"
"Para establecer una variable no es necesaro darle un parametro de entrada a la varaible simplemente con el dato de almacenamiento"
"Es posible utilizar Hints para parametrizar una varaible pero esto en un contexto más detallado pero puede existir una ambieguedad por el uso de datos almacenados"
"Posiblemnete sea una constante"

print("Tipo de Variables")
"-------------------------/"
"Variables de tipo texto"
"-------------------------/"
varaibleString = "Variable de tipo String o cadena String"
VariableTipoChart = 'N'
print("Uso de concatenación")

"-------------------------/"
"Variables Numericas"
"-------------------------/"
variableNumericaOInt = 1 #entero
variableNumeroFlotante = 1.2 #flotante
VariableTipoDouble = 1.202020 #double

print(f"variable int : {variableNumericaOInt} \nVariable punto flotante (Decimal) : {variableNumeroFlotante} \nVariable tipo Double o largas XD : {VariableTipoDouble}")
"-------------------------/"
"Variables Booleanas"
"-------------------------/"
variableTipoBoolean = False
print(f"Variable de tipo Boolean : {variableTipoBoolean}")
"-------------------------/"
"Operaciones con variables"
"-------------------------/"
print("----------Operaciones con variable---------------/")
suma = variableNumericaOInt + variableNumeroFlotante
resta = variableNumericaOInt - variableNumeroFlotante
multi = variableNumericaOInt * variableNumeroFlotante

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multi}")

print("\n----------Buffer de Datos en Ram o Dirección de memoria de las variables de  python---------------/\n")

print("***Explicación:***\nLa dirrección de memoria se encarga de mapear el enrutamiento de los procesos o almacenamiento de variables durante el proceso del codigo"
      "\nEl numero de procesamiento en la Ram se define por medio de la utilidad de la misma para el proceso"
      "\nUtilizado para la gestión y verificar del consumo de datos durante el proceso del software"
      "\nSe define de la siguiente forma por ser un numero Hexadecimal(16^) X_ULTIMOS_3_DIGITOS")
print(id(suma))
print(id(resta))
print(id(multi))