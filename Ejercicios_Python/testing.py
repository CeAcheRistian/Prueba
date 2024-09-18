from datetime import datetime, date #PARA TRABAJAR CON FECHAS
import unittest #Para crear test más robustos se importa la librería de unittest
#Con el testing se busca bajar la complejidad del código

def sumar(num1,num2):
    #En caso que los argumentos no sean enteros o decimales, lo acotamos
    if not isinstance(num1, (int,float)) or not isinstance(num2, (int,float)):
        raise ValueError("Los argumentos deben ser enteros o decimales") #Se procura cachar los errores más habituales
    return num1 + num2

#Para testear funciones se usa assert, con la llamada de la función ==  el resultado que se espera, sino se cumple, se lanza una excepcion
assert(sumar(10,2) == 12)

#Para lanzar varios test y tener una comprobación más robusta se crea la clase y funciones
#se crea una clase de Test<nombre> que herede de unittest.TestCase
class TestSumar(unittest.TestCase):
    #Se definen varios test como métodos de la clase test_<nombredeltest>
    def test_1(self):
        self.assertEqual(sumar(10,15), 25)

        #Aquí cachamos que sí se lance un error en específico 
        with self.assertRaises(ValueError): 
            sumar("5", 15)
        with self.assertRaises(ValueError): #Cada test es muy individual, particular al caso o atómico. 
            sumar(5, '15')
        with self.assertRaises(ValueError): #Para este punto, podemos ahcer test casi infinitos y la idea es abarcar los casos más generales o más habituales
            sumar(None, 15)

dicc = {
    'nombre': 'Chris',
    'edad': 27,
    'fecha_nacimiento': datetime.strptime('01/07/97','%d/%m/%y').date(), #el metodo strptime pasa de una cadena de texto a un objeto de tipo fecha.
    #El primer agumento es la fecha en string y el segundo es el formato. La fecha resultante manda a llamar al metodo date, el cual limita la respuesta a una fecha, ignorando las horas y minutos que el strptime da por defecto
    'lenguajes': ['Python', 'JavaScript']
}

#se crea una clase de Test<nombre> que herede de unittest.TestCase
class TestDiccionario(unittest.TestCase):
    """     El como se me ocurrió a mi:
    def test_1(self):
        #Test que verifica si existen las llaves y que los valores no sean False
        self.assertTrue(dicc['nombre'])
        self.assertTrue(dicc['edad'])
        self.assertTrue(dicc['fecha_nacimiento'])
        self.assertTrue(dicc['lenguajes'])

    def test_2(self):
        self.assertEqual(dicc['nombre'], 'Chris')
        self.assertEqual(dicc['edad'], 27)
        self.assertEqual(dicc['fecha_nacimiento'], '01/07/97')
        self.assertEqual(dicc['lenguajes'], ['Python', 'JavaScript'])"""

    #Los test tienen un "contexto" que son variables o datos con los que va a trabajar los test. Este contexto es un método de nombre setUp()
    def setUp(self) -> None: 
        #Y aquí dentro le metemos la data
        self.dicc = {
            'nombre': 'Chris',
            'edad': 27,
            'fecha_nacimiento': datetime.strptime('01/07/97','%d/%m/%y').date(),
            'lenguajes': ['Python', 'JavaScript']
        }
    
    def test_datos_existentes(self):
        #Con assertIn comprobamos que haya una instancia o elemento dentro de algun objeto
        self.assertIn("nombre", self.dicc)
        self.assertIn("edad", self.dicc)
        self.assertIn("fecha_nacimiento", self.dicc)
        self.assertIn("lenguajes", self.dicc) 

    def test_dato_correcto(self): #En los test no es pecado si el nombre del test es largo, lo importante es que se entienda que es lo que hace
        #Se aplica para los tipos de datos que sean los correctos. Pensando que el diccionario lo rellenan diferentes usuarios.
        self.assertIsInstance(self.dicc['nombre'], str)
        self.assertIsInstance(self.dicc['edad'], int)
        self.assertIsInstance(self.dicc['fecha_nacimiento'], date)
        self.assertIsInstance(self.dicc['lenguajes'], list)

#Para correr los test
if __name__ == "__main__":
    unittest.main()