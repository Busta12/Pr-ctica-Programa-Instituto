import unittest
from estudiante import Estudiante
import io
import sys

class TestEstudiante(unittest.TestCase):

    def setUp(self):
        self.estudiante = Estudiante("Juan", 25, "Mexico", 12345)

    def test_imprimirNombre(self):
        self.assertEqual(self.estudiante.nombre, "Juan")

    def test_imprimirEdad(self):
        self.assertEqual(self.estudiante.edad, 25)

    def test_imprimirPais(self):
        self.assertEqual(self.estudiante.pais, "Mexico")

    def test_imprimirMatricula(self):
        self.assertEqual(self.estudiante.matricula, 12345)

    def test_imprimirDatos(self):
        expected_output = "Nombre: Juan\nEdad: 25\nPais: Mexico\nMatrícula: 12345\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.estudiante.imprimirDatos()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()