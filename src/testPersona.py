import unittest
from persona import Persona
from io import StringIO
import sys

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.persona = Persona("Juan", 25, "Mexico")

    def test_initialization(self):
        self.assertEqual(self.persona.nombre, "Juan")
        self.assertEqual(self.persona.edad, 25)
        self.assertEqual(self.persona.pais, "Mexico")

    def test_imprimirNombre(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.persona.imprimirNombre()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Nombre:  Juan")

    def test_imprimirEdad(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.persona.imprimirEdad()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Edad:  25")

    def test_imprimirPais(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.persona.imprimirPais()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Pais:  Mexico")

    def test_imprimirDatos(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.persona.imprimirDatos()
        sys.stdout = sys.__stdout__
        expected_output = "Nombre:  Juan\nEdad:  25\nPais:  Mexico"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()