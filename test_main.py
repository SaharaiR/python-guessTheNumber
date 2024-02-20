import unittest
from main import generateNumber,resolveNumber #importamos del modulo la clase que queremos testear
from unittest.mock import patch
from io import StringIO

#Por convencion los nombres de las clases en python deben de ir con mayúsculas
"""
-En testing para python tiene clases bases que proporcionan un conjunto de metodos y funciones para 
facilitar la escritura y ejecución de pruebas unitarias, en este caso se puede usar "TestCase"
-Uso de mocks, al igual que en js, hay que simular un valor dado por el usuario para comprobrar lo 
esperado en el programa
-Los nombres de los métodos de prueba deben de empezar con "test_" para ser detectados automáticamente
-"assertTrue" es proporcionado por el objeto "self" (instancia de TestCase) y verifica que la expresión dentro
de los parentesis sea True
"""
class TestMain(unittest.TestCase):
    #Un test sería comprobar que se genera un numero aleatorio entre 1 y 100
    def test_generateNumber(self):
        number = generateNumber()
        self.assertTrue(1 <= number <= 100)

    """
    def setUp(self):
        # Configuramos el parche en el método 'setUp' para que se aplique a cada método de prueba
        self.mock_stdout_patch = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.mock_stdout_patch.start()

    def tearDown(self):
        # Detenemos el parche en el método 'tearDown' para limpiar después de cada prueba
        self.mock_stdout_patch.stop()
    """
    #Un test sería comprobar que el numero proporcionado por el usuario sea mayor, menor o igual
    """
    patch indica que el siguiente objeto o función será reemplazado temporalmente por algo 
    diferente durante la ejecución de la prueba.
    en este caso se sustituira lo que presenta en consola (sys.stdout)
    y "new_callable=StringIO" indica que se utilizar un nuevo objeto StringIO y al utilizar como
    new_callable indica que la salida estándar será sustituida por un objeto StringIO
    """
    @patch('sys.stdout', new_callable=StringIO)
    #self es una convención para utilizar como primer parametro. Se refiere a la instancia de la clase,
    #proporciona acceso a los métodos y atributos de la clase de prueba y el otro parametro para recibir
    #para recibir el objeto de parche (el mock) que es la salida stándar
    def test_resolveNumber(self,mock_stdout):
        numberToGuess = 10
        numberToResolve = 20 
        printExpected = resolveNumber(numberToGuess, numberToResolve)
        #capturamos la salida en pantalla, mock_stdout es el objeto, obtenemos el valor (getvalue) y con strip
        #se eliminan los espacios en blanco al inicio o final
        output = mock_stdout.getvalue().strip()
        #comparar la salida con la esperada
        self.assertEqual(output, "El número fue muy alto")
        self.assertIsNone(printExpected)
    
    #pass #palabra reservada para indicar que aquí va código que aún no se hace pero para que no marque error

if __name__ == '__main__':
    unittest.main()