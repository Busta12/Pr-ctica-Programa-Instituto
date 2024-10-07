import unittest
from grupo import Grupo
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante
from materia import Materia
from io import StringIO
import sys

class TestGrupo(unittest.TestCase):

    def setUp(self):
        self.curso = Curso("Python", "6 semanas")
        self.profesor = Profesor("Pedro", 35, "Mexico", 54321)
        self.estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
        self.estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
        self.materia = Materia("Programación", self.curso, self.profesor, [self.estudiante1, self.estudiante2])
        self.grupo = Grupo("Grupo A", self.materia)

    def test_imprimirNombre(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.grupo.imprimirNombre()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Nombre del grupo: Grupo A")

    def test_imprimirMateria(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.grupo.imprimirMateria()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Materia del grupo: Programación")

    def test_imprimirProfesor(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.grupo.imprimirProfesor()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Profesor del grupo: Pedro")

    def test_imprimirEstudiantes(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.grupo.imprimirEstudiantes()
        sys.stdout = sys.__stdout__
        expected_output = "Estudiantes del grupo:\nJuan\nMaria"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()