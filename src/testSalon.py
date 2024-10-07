# src/test_salon.py

import unittest
from salon import Salon
from grupo import Grupo
from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante

class TestSalon(unittest.TestCase):

    def setUp(self):
        curso = Curso("Python", "6 semanas")
        profesor = Profesor("Pedro", 35, "Mexico", 54321)
        estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
        estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
        materia = Materia("Programación", curso, profesor, [estudiante1, estudiante2])
        grupo = Grupo("Grupo A", materia)
        self.salon = Salon("Salón 101", grupo)

    def test_imprimirNombre(self):
        self.assertEqual(self.salon.nombre, "Salón 101")

    def test_imprimirGrupo(self):
        self.assertEqual(self.salon.grupo.nombre, "Grupo A")

    def test_imprimirCurso(self):
        self.assertEqual(self.salon.grupo.materia.nombre, "Programación")

    def test_imprimirProfesor(self):
        self.assertEqual(self.salon.grupo.materia.profesor.nombre, "Pedro")

    def test_imprimirEstudiantes(self):
        estudiantes_nombres = [estudiante.nombre for estudiante in self.salon.grupo.materia.estudiantes]
        self.assertIn("Juan", estudiantes_nombres)
        self.assertIn("Maria", estudiantes_nombres)

if __name__ == '__main__':
    unittest.main()