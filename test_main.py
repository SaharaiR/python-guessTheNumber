import unittest
from main import adivinaNumero #importamos del modulo la clase que queremos testear

#Por convencion los nombres de las clases en python deben de ir con mayúsculas
"""
En testing para python tiene clases bases que proporcionan un conjungo de metodos y funciones para 
facilitar la escritura y ejecución de pruebas unitarias, en este caso se puede usar "TestCase"
Uso de mocks, al igual que en js, hay que simular para comprobrar lo esperado en el programa
"""
class TestMain(unittest.TestCase):
    #Un test sería comprobar que el numero proporcionado por el usuario sea mayor, menor o igual
    pass #palabra reservada para indicar que aquí va código que aún no se hace pero para que no marque error