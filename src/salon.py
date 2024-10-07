
"""
This module defines a `Salon` class and demonstrates its usage.
Classes:
    Salon: Represents a classroom with a name and a group.
Methods:
    __init__(self, nombre, grupo): Initializes a new instance of the Salon class.
    imprimirNombre(self): Prints the name of the classroom.
    imprimirGrupo(self): Prints the name of the group associated with the classroom.
    imprimirCurso(self): Prints the name of the course associated with the classroom.
    imprimirProfesor(self): Prints the name of the professor associated with the classroom.
    imprimirEstudiantes(self): Prints the names of the students in the classroom.
Usage:
    The module demonstrates the creation of a `Salon` instance and calls its methods to print details about the classroom, group, course, professor, and students.
"""
#crear una clase llamada salon
#crear un metodo que imprima el nombre del salon
#crear un metodo que imprima el grupo del salon
#crear un metodo que imprima el curso del salon
#crear un metodo que imprima el profesor del salon
#crear un metodo que imprima los estudiantes del salon
#crear una instancia de la clase salon

from grupo import Grupo
from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante

class Salon:
    def __init__(self, nombre, grupo):
        self.nombre = nombre
        self.grupo = grupo

    def imprimirNombre(self):
        print("Nombre del salón:", self.nombre)

    def imprimirGrupo(self):
        print("Grupo del salón:", self.grupo.nombre)

    def imprimirCurso(self):
        print("Curso del salón:", self.grupo.materia.nombre)

    def imprimirProfesor(self):
        print("Profesor del salón:", self.grupo.materia.profesor.nombre)

    def imprimirEstudiantes(self):
        print("Estudiantes del salón:")
        for estudiante in self.grupo.materia.estudiantes:
            print(estudiante.nombre)

curso = Curso("Python", "6 semanas")
profesor = Profesor("Pedro", 35, "Mexico", 54321)
estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])
grupo = Grupo("Grupo A", materia)
salon = Salon("Salón 101", grupo)
salon.imprimirNombre()
salon.imprimirGrupo()
salon.imprimirCurso()
salon.imprimirProfesor()
salon.imprimirEstudiantes()
