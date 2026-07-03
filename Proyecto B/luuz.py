import random
dado=int(input("Ingrese cuantas veces tira el dado"))
cantidad=0
for i in range(dado):
    dado=random.randint(1,6)
    cantidad=cantidad+dado
    print("La sumatoria es",cantidad)