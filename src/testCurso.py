# src/test_curso.py

import unittest
from curso import Curso
from io import StringIO
import sys

class TestCurso(unittest.TestCase):
    def setUp(self):
        self.curso = Curso("Python", "6 semanas")

    def test_initialization(self):
        self.assertEqual(self.curso.nombre, "Python")
        self.assertEqual(self.curso.duracion, "6 semanas")

    def test_imprimirNombre(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.curso.imprimirNombre()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Nombre del curso: Python")

    def test_imprimirDuracion(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.curso.imprimirDuracion()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Duración del curso: 6 semanas")

if __name__ == '__main__':
    unittest.main()