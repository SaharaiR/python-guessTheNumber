import random

print("¡Bienvenido a ADIVINA EL NÚMERO!")
print("Por favor escribe cualquier número entre 1 y 100: ")
guessing = input('--> ')
print(guessing)

toGuess = random.randint(1,100)
print(toGuess)