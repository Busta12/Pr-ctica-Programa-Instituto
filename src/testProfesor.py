import unittest
from profesor import Profesor
import io
import sys

class TestProfesor(unittest.TestCase):

    def setUp(self):
        self.profesor = Profesor("Pedro", 35, "Mexico", 54321)

    def test_initialization(self):
        self.assertEqual(self.profesor.nombre, "Pedro")
        self.assertEqual(self.profesor.edad, 35)
        self.assertEqual(self.profesor.pais, "Mexico")
        self.assertEqual(self.profesor.id_profesor, 54321)

    def test_imprimirIdProfesor(self):
        expected_output = "ID Profesor: 54321\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.profesor.imprimirIdProfesor()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_imprimirDatos(self):
        expected_output = "Nombre: Pedro\nEdad: 35\nPais: Mexico\nID Profesor: 54321\n"
        captured_output = io.StringIO()
        sys.stdout = captured_output
        self.profesor.imprimirDatos()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()