
"""
This module defines the Escuela class and demonstrates its usage.
Classes:
    Escuela: Represents a school with methods to print its details.
Methods:
    __init__(self, nombre, salon): Initializes the Escuela instance with a name and a salon.
    imprimirNombre(self): Prints the name of the school.
    imprimirSalon(self): Prints the name of the salon.
    imprimirGrupo(self): Prints the name of the group.
    imprimirCurso(self): Prints the name of the course.
    imprimirProfesor(self): Prints the name of the professor.
    imprimirEstudiantes(self): Prints the names of the students.
Usage:
    The module imports several classes (Grupo, Materia, Curso, Profesor, Estudiante, Salon) 
    and creates instances of these classes to demonstrate the functionality of the Escuela class.
"""
#crear una clase llamada escuela
#crear un metodo que imprima el nombre de la escuela
#crear un metodo que imprima el salon de la escuela
#crear un metodo que imprima el grupo de la escuela
#crear un metodo que imprima el curso de la escuela
#crear un metodo que imprima el profesor de la escuela
#crear un metodo que imprima los estudiantes de la escuela
#crear una instancia de la clase escuela

from grupo import Grupo
from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante
from salon import Salon

class Escuela:
    def __init__(self, nombre, salon):
        self.nombre = nombre
        self.salon = salon

    def imprimirNombre(self):
        print("Nombre de la escuela:", self.nombre)

    def imprimirSalon(self):
        print("Salón de la escuela:", self.salon.nombre)

    def imprimirGrupo(self):
        print("Grupo de la escuela:", self.salon.grupo.nombre)

    def imprimirCurso(self):
        print("Curso de la escuela:", self.salon.grupo.materia.curso.nombre)

    def imprimirProfesor(self):
        print("Profesor de la escuela:", self.salon.grupo.materia.profesor.nombre)

    def imprimirEstudiantes(self):
        print("Estudiantes de la escuela:")
        for estudiante in self.salon.grupo.materia.estudiantes:
            print(estudiante.nombre)

curso = Curso("Python", "6 semanas")
profesor = Profesor("Pedro", 35, "Mexico", 54321)
estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])
grupo = Grupo("Grupo A", materia)
salon = Salon("Salón 101", grupo)
escuela = Escuela("Code", salon)
escuela.imprimirNombre()
escuela.imprimirSalon()
escuela.imprimirGrupo()
escuela.imprimirCurso()
escuela.imprimirProfesor()
escuela.imprimirEstudiantes()
