import random
#Creando la función
def TirarDados(cantidad):
    suma=0
    for i in range(cantidad):
     dado=random.randint(1,6)
     suma=suma+dado
     return suma
#uso de la función es un programa principal
jugador1=int(input("Cuantas veces tira el dado"))
resultado1=TirarDados (jugador1)
print("jugador 1 sacó", resultado1)
jugador2=int(input("Cuantas veces tira el dado"))
resultado2=TirarDados (jugador2)
print("jugador 2 sacó", resultado2)