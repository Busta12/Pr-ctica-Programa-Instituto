
"""
This module defines the Materia class and demonstrates its usage.
Classes:
    Materia: Represents a subject with a name, course, professor, and students.
Usage:
    The Materia class includes methods to print the name of the subject, the course, the professor, and the students.
Example:
"""

#crear una clase llamada materia
#crear un metodo que imprima el nombre de la materia
#crear un metodo que imprima el curso de la materia
#crear un metodo que imprima el profesor de la materia
#crear un metodo que imprima los estudiantes de la materia
#crear una instancia de la clase materia

from curso import Curso
from profesor import Profesor
from estudiante import Estudiante

class Materia:
    def __init__(self, nombre, curso, profesor, estudiantes):
        self.nombre = nombre
        self.curso = curso
        self.profesor = profesor
        self.estudiantes = estudiantes

    def imprimirNombre(self):
        print("Nombre de la materia:", self.nombre)

    def imprimirCurso(self):
        print("Curso de la materia:", self.curso.nombre)

    def imprimirProfesor(self):
        print("Profesor de la materia:", self.profesor.nombre)

    def imprimirEstudiantes(self):
        print("Estudiantes de la materia:")
        for estudiante in self.estudiantes:
            print(estudiante.nombre)

curso = Curso("Python", "6 semanas")
profesor = Profesor("Pedro", 35, "Mexico", 54321)
estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
materia1 = Materia("Programación", curso, profesor, [estudiante1, estudiante2])
materia1.imprimirNombre()
materia1.imprimirCurso()
materia1.imprimirProfesor()
materia1.imprimirEstudiantes()
