
"""
This module defines the Profesor class, which inherits from the Persona class.
Classes:
    Profesor: A class representing a professor, inheriting from Persona.
Methods:
    __init__(self, nombre, edad, pais, id_profesor): Initializes a new instance of the Profesor class.
    imprimirIdProfesor(self): Prints the ID of the professor.
    imprimirDatos(self): Prints all the data of the professor, including the ID.
Example:
"""

#crear una clase llamada profesor que herede de la clase persona
#crear un metodo que imprima el nombre del profesor
#crear un metodo que imprima la edad del profesor
#crear un metodo que imprima el pais de origen del profesor
#crear un metodo que imprima todos los datos del profesor
#crear una instancia de la clase profesor

from persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, edad, pais, id_profesor):
        super().__init__(nombre, edad, pais)
        self.id_profesor = id_profesor

    def imprimirIdProfesor(self):
        print("ID Profesor:", self.id_profesor)

    def imprimirDatos(self):
        super().imprimirDatos()
        print("ID Profesor:", self.id_profesor)

profesor1 = Profesor("Pedro", 35, "Mexico", 54321)
profesor1.imprimirNombre()
profesor1.imprimirEdad()
profesor1.imprimirPais()
profesor1.imprimirDatos()

