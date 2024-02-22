import random
import sys
#from random import randint
#Para hacer testing tenemos que tener funciones o métodos [def]
"""
Entonces las funciones:
    1. Función principal (guessNumber)
    2. Generar numero aleatorio (generateNumber)
    3. Comparar el número y resolver si es menor, mayor o igual (resolveNumber)
    4. Empezar nuevo juego (newGame)
    Las tres se van a llamar dentro del bucle en determinado momento

"""

def guessNumber():
    #En python el tipado es dinámico, según el valor asignado es el tipo de dato de la variable
    print("¡Bienvenido a ADIVINA EL NÚMERO!")
    print("Tendrás tu turno para adivinar el número y luego será mi turno, cuando se adivine se termina el juego")
    print("¿Cuál es tu nombre?", end= " ")
    nameUser = input(": ")
    if not nameUser.isspace():
        nameUser = "Desconocido"
    print(nameUser + ", escribe un número entero entre 1 y 100: ")
    guessingUser = input('--> ')
    #validar la entrada del usuario
    validate = validateInput(guessingUser)
    while validate == False:
        print("Por favor, escribe un número válido, recuerda que tiene que ser un entero entre 1 y 100")
        guessingUser = input('--> ')
        validate = validateInput(guessingUser)
    #convertir a entero, ya que el valor inicial lo guarda como cadena
    guessingUser = int(guessingUser)
    #se declararn las listas para ir guardando los intentos
    attempsUser = []
    attempsPC = []
    attempsUser.append(guessingUser)
    toGuess = generateNumber()
    #while guessingUser != toGuess:
    #Cambie a un bucle infinito hasta que encuentre los break
    while True:
        #print(toGuess)
        findItUser = resolveNumber(toGuess, guessingUser)
        printResolve(findItUser)
        if findItUser == True:
            print("¡" + nameUser + " has adivinado el número!")
            print("Tus intentos fueron: ", end=" ")
            print(attempsUser)
            break
        guessingPC = generateNumber()
        attempsPC.append(guessingPC)
        print(" ")
        print("--Mi turno: ", end=" ")
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
        print("--Turno de " + nameUser + "--")
        print("No haz adivinado el número, intenta de nuevo ", end=" ")
        guessingUser = int(input(': '))
        attempsUser.append(guessingUser)
    newGame()
                
def generateNumber():
    return random.randint(1,10)

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

def validateInput(numberToValidate):
    #si no es un numero entero
    if not numberToValidate.isdigit() or not numberToValidate.strip():
        return False
    else:
        return True

if __name__ == "__main__":
    guessNumber()

"""
__name__ es una variable especial que Python asigna dependiendo de cómo se esté utilizando el script. 
Cuando el script es ejecutado directamente, __name__ se establece en "__main__". 
Por lo tanto, este bloque de código se ejecutará solo si el script es el programa 
principal que se está ejecutando.
"""