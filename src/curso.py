
"""
This module defines a `Curso` class with methods to print the course name and duration.
Classes:
    Curso: A class to represent a course with a name and duration.
Methods:
    __init__(self, nombre, duracion): Initializes the course with a name and duration.
    imprimirNombre(self): Prints the name of the course.
    imprimirDuracion(self): Prints the duration of the course.
Example:
"""
#crear una clase llamada curso
#crear un metodo que imprima el nombre del curso
#crear un metodo que imprima la duracion del curso
#crear una instancia de la clase curso

class Curso:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

    def imprimirNombre(self):
        print("Nombre del curso:", self.nombre)

    def imprimirDuracion(self):
        print("Duración del curso:", self.duracion)

curso1 = Curso("Python", "6 semanas")
curso1.imprimirNombre()
curso1.imprimirDuracion()

