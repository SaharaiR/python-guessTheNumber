import random
#from random import randint

print("¡Bienvenido a ADIVINA EL NÚMERO!")
print("Por favor escribe cualquier número entre 1 y 100: ")
#En python el tipado es dinámico, según el valor asignado es el tipo de dato de la variable
guessing = int(input('--> '))
#print(guessing)
toGuess = random.randint(1,100)
print(toGuess)

while guessing != toGuess:
    #convertir a entero, ya que lo guarda como cadena
    if(guessing > toGuess):
        print("El número es muy alto")
    if(guessing < toGuess):
        print("El número es muy bajo")
    print("No haz adivinado el número, intenta de nuevo: ")
    guessing = int(input('--> '))
print("¡Felicidades haz adivinado el número!")