# src/test_materia.py

import unittest
from materia import Materia
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante
from io import StringIO
import sys

class TestMateria(unittest.TestCase):
    def setUp(self):
        self.curso = Curso("Python", "6 semanas")
        self.profesor = Profesor("Pedro", 35, "Mexico", 54321)
        self.estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
        self.estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
        self.materia = Materia("Programación", self.curso, self.profesor, [self.estudiante1, self.estudiante2])

    def test_imprimirNombre(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.materia.imprimirNombre()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Nombre de la materia: Programación")

    def test_imprimirCurso(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.materia.imprimirCurso()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Curso de la materia: Python")

    def test_imprimirProfesor(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.materia.imprimirProfesor()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Profesor de la materia: Pedro")

    def test_imprimirEstudiantes(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.materia.imprimirEstudiantes()
        sys.stdout = sys.__stdout__
        expected_output = "Estudiantes de la materia:\nJuan\nMaria"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()