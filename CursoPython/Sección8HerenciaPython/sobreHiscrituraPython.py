from ClasePadrePersona import Persona
class Director(Persona):

    def __init__(this, nombre,apellido,salary,superCargo):
        super().__init__(nombre,apellido)
        this.__salary = salary
        this.__superCargo = superCargo

#Salario-------------------------------------------------------------
    @property
    def salary(this):
        return this.__salary

    @salary.setter
    def salary(this,salaryNew):
        this.__salary = salaryNew

#SuperCargo----------------------------------------------------------------

    @property
    def superCargo(this):
        return this.__superCargo

    @superCargo.setter
    def superCargo(this,otherWork):
        this.__superCargo = otherWork


#Comportamiento_BASE

    def __str__(this):
        return f"Salida basica por sobre escritura delimitando y quitando el STR : " \
               f"{super().__str__()}" \
               f" Salario : {this.__salary} Cargo : {this.__superCargo}"

    def salida_Basica(self):
        print(f"Salida basica de pantalla : "
              f"Name : {super().__name} Last Name : {super().__lastName} "
              f"Salario : {this.__salary}"
              f"Cargo : {this.__superCargo}")


direc1 = Director('Sergio','Linares','3000000','Director')
#print(direc1)


