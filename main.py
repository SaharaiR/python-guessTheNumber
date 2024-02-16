import random
#from random import randint
#Para hacer testing tenemos que tener funciones o métodos [def]
"""
Entonces 4 funciones:
    1. Función principal
    2. Generar numero aleatorio
    3. Interactuar con el usuario, pidiendo el numero y comparar
    4. Logica del ordenador, generando numero aleatorio y comparar
    Las tres se van a llamar dentro del bucle en determinado momento
"""

def guessNumber():
    print("¡Bienvenido a ADIVINA EL NÚMERO!")
    print("Por favor escribe cualquier número entre 1 y 100: ")
    #En python el tipado es dinámico, según el valor asignado es el tipo de dato de la variable
    #convertir a entero, ya que el valor inicial lo guarda como cadena
    global guessingUser 
    guessingUser = int(input('--> '))
    #print(guessing)
    #toGuess = random.randint(1,100)
    global toGuess 
    toGuess = generateNumber()
    #print(toGuess)
    #guessingPC = random.randint(1,100)
    #while guessingUser != toGuess:
    #Cambie a un bucle infinito hasta que encuentre los break
    while True:
        print(toGuess)
        
        findItUser = userLogic()
        if findItUser == True:
            break
        elif findItUser == False:
            findItPC = pcLogic()
            if findItPC == True:
                break
            elif findItPC == False:
                #Si no adivinó el ordenador le toca al usuario
                print("            ")
                print("--Tu turno--")
                print("No haz adivinado el número, intenta de nuevo: ")
                guessingUser = int(input('--> '))
        """
        if(guessingUser > toGuess):
            print("Tu número es muy alto")
        elif(guessingUser < toGuess):
            print("Tu número es muy bajo")
        elif(guessingUser == toGuess):
            print("¡Haz adivinado el número!")
            break
        """
        #Aquí tendria que ir la lógica del ordenador
        """
        print("            ")
        print("--Mi turno--")
        global guessingPc
        guessingPC = genearteNumber()
        print(guessingPC)
        if(guessingPC > toGuess):
            print("Mi número fue muy alto")
        elif(guessingPC < toGuess):
            print("Mi número fue muy bajo")
        elif(guessingPC == toGuess):
            print("¡He adivinado el número!")
            break
        #Se genera un nuevo nuevo aleatorio para el turno del ordenador
        guessingPC = random.randint(1,100)
        
        #Si no adivinó el ordenador le toca al usuario
        print("            ")
        print("--Tu turno--")
        print("No haz adivinado el número, intenta de nuevo: ")
        guessingUser = int(input('--> '))
        """

def generateNumber():
    return random.randint(1,100)

def userLogic():
    if(guessingUser > toGuess):
        print("Tu número es muy alto")
        return False
    elif(guessingUser < toGuess):
        print("Tu número es muy bajo")
        return False
    elif(guessingUser == toGuess):
        print("¡Haz adivinado el número!")
        return True

def pcLogic():
    print("            ")
    print("--Mi turno--")
    guessingPC = generateNumber()
    print(guessingPC)
    if(guessingPC > toGuess):
        print("Mi número fue muy alto")
        return False
    elif(guessingPC < toGuess):
        print("Mi número fue muy bajo")
        return False
    elif(guessingPC == toGuess):
        print("¡He adivinado el número!")
        return True

if __name__ == "__main__":
    guessNumber()

"""
__name__ es una variable especial que Python asigna dependiendo de cómo se esté utilizando el script. 
Cuando el script es ejecutado directamente, __name__ se establece en "__main__". 
Por lo tanto, este bloque de código se ejecutará solo si el script es el programa 
principal que se está ejecutando.
"""