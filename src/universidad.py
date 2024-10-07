"""
This module defines a Universidad class and demonstrates its usage.
Classes:
    Universidad: Represents a university with methods to print its details.
Usage:
    The Universidad class is instantiated with a name and a salon (classroom).
    It provides methods to print the university's name, salon, group, course, professor, and students.
Example:
"""
#crear una clase llamada universidad
#crear un metodo que imprima el nombre de la universidad
#crear un metodo que imprima el salon de la universidad
#crear un metodo que imprima el grupo de la universidad
#crear un metodo que imprima el curso de la universidad
#crear un metodo que imprima el profesor de la universidad
#crear un metodo que imprima los estudiantes de la universidad
#crear una instancia de la clase universidad

from grupo import Grupo
from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante
from salon import Salon

class Universidad:
    def __init__(self, nombre, salon):
        self.nombre = nombre
        self.salon = salon

    def imprimirNombre(self):
        print("Nombre de la universidad:", self.nombre)

    def imprimirSalon(self):
        print("Salón de la universidad:", self.salon.nombre)

    def imprimirGrupo(self):
        print("Grupo de la universidad:", self.salon.grupo.nombre)

    def imprimirCurso(self):
        print("Curso de la universidad:", self.salon.grupo.materia.curso.nombre)

    def imprimirProfesor(self):
        print("Profesor de la universidad:", self.salon.grupo.materia.profesor.nombre)

    def imprimirEstudiantes(self):
        print("Estudiantes de la universidad:")
        for estudiante in self.salon.grupo.materia.estudiantes:
            print(estudiante.nombre)

curso = Curso("Python", "6 semanas")
profesor = Profesor("Pedro", 35, "Mexico", 54321)
estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])
grupo = Grupo("Grupo A", materia)
salon = Salon("Salón 101", grupo)
universidad = Universidad("Code", salon)
universidad.imprimirNombre()
universidad.imprimirSalon()
universidad.imprimirGrupo()
universidad.imprimirCurso()
universidad.imprimirProfesor()
universidad.imprimirEstudiantes()
