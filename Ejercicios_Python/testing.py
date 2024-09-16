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
        self.assertEqual(sumar(10,15), 5)

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
    'fecha_nacimiento': '01/07/97',
    'lenguajes': ['Python', 'JavaScript']
}

#se crea una clase de Test<nombre> que herede de unittest.TestCase
class TestDiccionario(unittest.TestCase):
    
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
        self.assertEqual(dicc['lenguajes'], ['Python', 'JavaScript'])

#Para correr los test
if __name__ == "__main__":
    unittest.main()