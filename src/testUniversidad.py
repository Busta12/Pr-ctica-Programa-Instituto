import unittest
from universidad import Universidad
from curso import Curso
from profesor import Profesor
from estudiante import Estudiante
from materia import Materia
from grupo import Grupo
from salon import Salon
from io import StringIO
import sys

class TestUniversidad(unittest.TestCase):
    def setUp(self):
        self.curso = Curso("Python", "6 semanas")
        self.profesor = Profesor("Pedro", 35, "Mexico", 54321)
        self.estudiante1 = Estudiante("Juan", 25, "Mexico", 12345)
        self.estudiante2 = Estudiante("Maria", 22, "Colombia", 54321)
        self.materia = Materia("Programación", self.curso, self.profesor, [self.estudiante1, self.estudiante2])
        self.grupo = Grupo("Grupo A", self.materia)
        self.salon = Salon("Salón 101", self.grupo)
        self.universidad = Universidad("Code", self.salon)

    def test_imprimirNombre(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirNombre()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Nombre de la universidad: Code")

    def test_imprimirSalon(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirSalon()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Salón de la universidad: Salón 101")

    def test_imprimirGrupo(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirGrupo()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Grupo de la universidad: Grupo A")

    def test_imprimirCurso(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirCurso()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Curso de la universidad: Python")

    def test_imprimirProfesor(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirProfesor()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "Profesor de la universidad: Pedro")

    def test_imprimirEstudiantes(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.universidad.imprimirEstudiantes()
        sys.stdout = sys.__stdout__
        expected_output = "Estudiantes de la universidad:\nJuan\nMaria"
        self.assertEqual(captured_output.getvalue().strip(), expected_output)

if __name__ == '__main__':
    unittest.main()