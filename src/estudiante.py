

"""
This module defines the Estudiante class which inherits from the Persona class.
Classes:
    Estudiante(Persona): A class representing a student, inheriting from Persona.
Methods:
    __init__(self, nombre, edad, pais, matricula): Initializes an instance of the Estudiante class.
    imprimirMatricula(self): Prints the student's matricula.
Usage:
"""

#crear una clase llamada estudiante que herede de la clase persona
#crear un metodo que imprima el nombre del estudiante
#crear un metodo que imprima la edad del estudiante
#crear un metodo que imprima el pais de origen del estudiante
#crear un metodo que imprima todos los datos del estudiante
#crear una instancia de la clase estudiante
#crear una instancia de la clase persona

from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, pais, matricula):
        super().__init__(nombre, edad, pais)
        self.matricula = matricula

    def imprimirMatricula(self):
        print("Matrícula:", self.matricula)

    def imprimirDatos(self):
        super().imprimirDatos()
        print("Matrícula:", self.matricula)

estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante1.imprimirNombre()
estudiante1.imprimirEdad()
estudiante1.imprimirPais()
estudiante1.imprimirDatos()
estudiante1.imprimirMatricula()



