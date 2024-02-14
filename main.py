import random
#from random import randint
#Para hacer testing tenemos que tener funciones o métodos [def]

def adivinaNumero():
    print("¡Bienvenido a ADIVINA EL NÚMERO!")
    print("Por favor escribe cualquier número entre 1 y 100: ")
    #En python el tipado es dinámico, según el valor asignado es el tipo de dato de la variable
    guessingUser = int(input('--> '))
    #print(guessing)
    toGuess = random.randint(1,100)
    #print(toGuess)

    guessingPC = random.randint(1,100)
    #while guessingUser != toGuess:
    #Cambie a un bucle infinito hasta que encuentre los break
    while True:
        print(toGuess)
        #convertir a entero, ya que el valor inicial lo guarda como cadena
        if(guessingUser > toGuess):
            print("Tu número es muy alto")
        elif(guessingUser < toGuess):
            print("Tu número es muy bajo")
        elif(guessingUser == toGuess):
            print("¡Haz adivinado el número!")
            break

        #Aquí tendria que ir la lógica del ordenador
        print("            ")
        print("--Mi turno--")
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
    #print("¡Haz adivinado el numero!")