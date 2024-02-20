import random
import sys
#from random import randint
#Para hacer testing tenemos que tener funciones o métodos [def]
"""
Entonces las funciones:
    1. Función principal
    2. Generar numero aleatorio
    3. Comparar el número y resolver si es menor, mayor o igual
    Las tres se van a llamar dentro del bucle en determinado momento

"""

def guessNumber():
    print("¡Bienvenido a ADIVINA EL NÚMERO!")
    print("Por favor escribe cualquier número entre 1 y 100: ")
    #En python el tipado es dinámico, según el valor asignado es el tipo de dato de la variable
    #convertir a entero, ya que el valor inicial lo guarda como cadena
    attempsUser = []
    attempsPC = []
    guessingUser = int(input('--> '))
    attempsUser.append(guessingUser)
    #print(guessing)
    #toGuess = random.randint(1,100)
    toGuess = generateNumber()
    #print(toGuess)
    #guessingPC = random.randint(1,100)
    #while guessingUser != toGuess:
    #Cambie a un bucle infinito hasta que encuentre los break
    while True:
        #print(toGuess)
        findItUser = resolveNumber(toGuess, guessingUser)
        printResolve(findItUser)
        if findItUser == True:
            print("¡Haz adivinado el número!")
            print("Tus intentos fueron: ", end=" ")
            print(attempsUser)
            break
        guessingPC = generateNumber()
        attempsPC.append(guessingPC)
        print(" ")
        print("--MI TURNO: ", end=" ")
        print(guessingPC)
        findItPC = resolveNumber(toGuess, guessingPC)
        printResolve(findItPC)
        if findItPC == True:
            print("He adivinado el número")
            print("Mis intentos fueron: ", end=" ")
            print(attempsPC)
            break
        #Si no adivinó el ordenador le toca al usuario
        print(" ")
        print("--TU TURNO--")
        print("No haz adivinado el número, intenta de nuevo ", end=" ")
        guessingUser = int(input(': '))
        attempsUser.append(guessingUser)
    newGame()
                
def generateNumber():
    return random.randint(1,100)

def resolveNumber(toGuessNumber, guessingNumber):
    if(guessingNumber > toGuessNumber):
        return "high"
    elif(guessingNumber < toGuessNumber):
        return "low"
    elif(guessingNumber == toGuessNumber):
        return True

def printResolve(resolve):
    if(resolve == "high"):
        print("El número es muy alto")
    elif(resolve == "low"):
        print("El número es muy bajo")

def newGame():
    print("¿Quieres jugar de nuevo? (SI/NO) ", end=" ")
    answer = input(': ').lower()
    if answer == "si":
        guessNumber()
    elif answer == "no":
        print("Gracias por jugar")
        sys.exit()

if __name__ == "__main__":
    guessNumber()

"""
__name__ es una variable especial que Python asigna dependiendo de cómo se esté utilizando el script. 
Cuando el script es ejecutado directamente, __name__ se establece en "__main__". 
Por lo tanto, este bloque de código se ejecutará solo si el script es el programa 
principal que se está ejecutando.
"""