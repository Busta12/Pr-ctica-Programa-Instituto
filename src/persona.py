
"""
This module defines a `Persona` class with attributes for name, age, and country of origin.
It includes methods to print each attribute individually and a method to print all attributes together.
Classes:
    Persona
Methods:
    __init__(self, nombre, edad, pais):
        Initializes a new instance of the Persona class.
    imprimirNombre(self):
        Prints the name of the person.
    imprimirEdad(self):
        Prints the age of the person.
    imprimirPais(self):
        Prints the country of origin of the person.
    imprimirDatos(self):
        Prints all the details of the person (name, age, and country of origin).
Example:
"""
#crear una clase persona que tenga como atributos nombre, edad y pais de origen
#crear un metodo que imprima el nombre de la persona
#crear un metodo que imprima la edad de la persona
#crear un metodo que imprima el pais de origen de la persona
#crear un metodo que imprima todos los datos de la persona
#crear una instancia de la clase persona

class Persona:
    def __init__(self, nombre, edad, pais):
        self.nombre = nombre
        self.edad = edad
        self.pais = pais

    def imprimirNombre(self):
        print("Nombre: ", self.nombre)

    def imprimirEdad(self):
        print("Edad: ", self.edad)

    def imprimirPais(self):
        print("Pais: ", self.pais)

    def imprimirDatos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Pais: ", self.pais)

persona1 = Persona("Juan", 25, "Mexico")
persona1.imprimirNombre()
persona1.imprimirEdad()
persona1.imprimirPais()
persona1.imprimirDatos()
