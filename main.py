from random import choice
from os import system
from time import sleep

system("cls||clear")                                                            #limpiar la consola

print("Bienvenido a Piedra, papel o tijera!" + "\n")
print("Por favor, inserte el número su mano a jugar.")

hands = ["Piedra", "Papel", "Tijera"]                                           #manos a jugar


def select():
    print("1. " + hands[0])
    print("2. " + hands[1])
    print("3. " + hands[2])
    choice = input("Mano a jugar: ")                                            #mano del jugador, almacenamiento tipo str
    try:
        choice = int(choice)                                                    #convertir choice de str a int
    except ValueError:                                                          #ValueError: intentar convertir texto (no numérico) a entero
        system("cls||clear")
        print("Su respuesta no es válida. Escriba el número a jugar." + "\n")
        return
    if choice != 1 and choice != 2 and choice != 3:                             #si choice es un número distinto a 1, 2 o 3
        system("cls||clear")
        print("Por favor, ingrese uno de los números indicados." + "\n")
        return
    return (choice - 1)


handPlayer = select()                                                           #mano del jugador almacenado en la variable handPlayer
while type(handPlayer) != int:                                                  #si handPlayer no es int (no se ejecutó correctamente)
    handPlayer = select()                                                       #la función select se repite en bucle hasta que handPlayer sea int

print("\n" + "La mano seleccionada es: " + hands[handPlayer]), sleep(1.5)       #sleep para simular tiempo de elección de la mano rival

handCPU = choice(hands)

print("Tu oponente ha elegido qué jugar. Preparense!" + "\n")

ready1 = "Piedra...... Papel...... "
ready2 = "TIJERA!!!"

for i in range(len(ready1)):
    print(ready1[i], end=""), sleep(0.07)                                       #animación de escritura de texto ready1 progresivo

for i in range(len(ready2)):
    print(ready2[i], end=""), sleep(0.02)                                       #animación de escritura de texto ready2 progresivo

print("\n \n" + "Has jugado: " + hands[handPlayer])
print("Tu oponente jugó: " + handCPU + "\n")

results = []
results.append(hands[handPlayer])                                               #guardar mano del jugador en array results
results.append(handCPU)                                                         #guardar mano rival en array results

if hands[0] in results and hands[1] in results:                                 #caso piedra y papel en array results
    if hands[handPlayer] == hands[1]:                                           #si la mano ganadora es del jugador...
        print("Felicidades, has ganado!")
    else:
        print("Has perdido, mejor suerte la próxima.")

elif hands[1] in results and hands[2] in results:                               #caso papel y tijera en array results
    if hands[handPlayer] == hands[2]:                                           #si la mano ganadora es del jugador...
        print("Felicidades, has ganado!")
    else:
        print("Has perdido, mejor suerte la próxima.")

elif hands[2] in results and hands[0] in results:                               #caso tijera y piedra en array results
    if hands[handPlayer] == hands[0]:                                           #si la mano ganadora es del jugador...
        print("Felicidades, has ganado!")
    else:
        print("Has perdido, mejor suerte la próxima.")

else:                                                                           #caso manos iguales (empate)
    print("Ambos jugaron la misma mano. Es un empate.")