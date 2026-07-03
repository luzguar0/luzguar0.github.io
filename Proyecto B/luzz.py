monedas=int(input("ingrese las monedas que juntó"))
puntaje=0
while(monedas!=-1):
    puntaje=puntaje+monedas
    monedas=int(input("ingrese las monedas que juntó"))
print("Puntaje final",puntaje)