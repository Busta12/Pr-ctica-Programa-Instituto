
"""
This module defines the Grupo class and demonstrates its usage.

Classes:
    Grupo: A class to represent a group with a specific subject (materia).

Methods:
    __init__(self, nombre, materia): Initializes the Grupo instance with a name and a Materia instance.
    imprimirNombre(self): Prints the name of the group.
    imprimirMateria(self): Prints the name of the subject (materia) of the group.
    imprimirProfesor(self): Prints the name of the professor of the group.
    imprimirEstudiantes(self): Prints the names of the students in the group.

Example:
    # Crear instancias de Curso, Profesor y Estudiantes
    curso = Curso("Python", "6 semanas")
    profesor = Profesor("Pedro", 35, "Mexico", 54321)
    estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
    estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)

    # Crear una instancia de Materia
    materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])

    # Crear una instancia de Grupo
    grupo1 = Grupo("Grupo A", materia)

    # Imprimir los datos del grupo
    grupo1.imprimirNombre()
    grupo1.imprimirMateria()
    grupo1.imprimirProfesor()
    grupo1.imprimirEstudiantes()
"""
#crear una clase llamada grupo
#crear un metodo que imprima el nombre del grupo
#crear un metodo que imprima el curso del grupo
#crear un metodo que imprima el profesor del grupo
#crear un metodo que imprima los estudiantes del grupo
#crear una instancia de la clase grupo

from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante

class Grupo:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia

    def imprimirNombre(self):
        print("Nombre del grupo:", self.nombre)

    def imprimirMateria(self):
        print("Materia del grupo:", self.materia.nombre)

    def imprimirProfesor(self):
        print("Profesor del grupo:", self.materia.profesor.nombre)

    def imprimirEstudiantes(self):
        print("Estudiantes del grupo:")
        for estudiante in self.materia.estudiantes:
            print(estudiante.nombre)

# Crear instancias de Curso, Profesor y Estudiantes
curso = Curso("Python", "6 semanas")
profesor = Profesor("Pedro", 35, "Mexico", 54321)
estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)

# Crear una instancia de Materia
materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])

# Crear una instancia de Grupo
grupo1 = Grupo("Grupo A", materia)

# Imprimir los datos del grupo
grupo1.imprimirNombre()
grupo1.imprimirMateria()
grupo1.imprimirProfesor()
grupo1.imprimirEstudiantes()
