import unittest
from main import generateNumber #importamos del modulo la clase que queremos testear

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
        numero = generateNumber()
        self.assertTrue(1 <= numero <= 100)
    #Un test sería comprobar que el numero proporcionado por el usuario sea mayor, menor o igual
    
    #pass #palabra reservada para indicar que aquí va código que aún no se hace pero para que no marque error

if __name__ == '__main__':
    unittest.main()