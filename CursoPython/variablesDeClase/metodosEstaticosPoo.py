class newClas():
    imAVarOfClas = "Hello"

    def __init__(this,a):
        this.a = a

    @staticmethod #Se determina una función estatica (No esta asosiada a la instancia entre clases pero
    #Si a la clase misma)
    #No necesita de el self o this porque no es una función de instancia
    #Para llamar variables de clase necesita declarar la clase primero
    def hello():
        print(newClas.imAVarOfClas) #Metodos Estaticos
              #instancia clase
    @classmethod #Esta Función tiene como objetivo
                 #CLS es utilizado para referirse a la clase
                 #Y la principal diferencia es que cls trae variables de clase
                 # sin necesidad de llamar a la clase solo utilizando CLS
    def nello2(cls):
        print(cls.imAVarOfClas) #Metodo de clase
            #instancia cls para variables de clae

    #metodo de instancia con self o this (Contexto dinamico)
    def hello3(self):
        #Variables de instancia
        #Varaibles de clase
        #Variables asociadas con el obj creado
        #Podemos llamar metodos de clase
            self.nello2() #Utilizando self y metodo de clase
            self.hello() #Metodo  estatico

#SE HACE EL LLAMADO INPLICITO CON LA CLASE Y SIN CONSTRUCTOR
newClas.hello()
newClas.nello2()

obj1 = newClas('Hello') #Creando un objeto nosotros podemos acceder a los metodos de intancia y de clase
obj1.nello2()
obj1.nello2()
obj1.imAVarOfClas #Variable de instancia 

#Contexto estatico son las funciones o varaibles que e determinan en la clase.
#Contexto dinamico son las funciones o varaibles que se determinan en al realizar una instancia de clase
