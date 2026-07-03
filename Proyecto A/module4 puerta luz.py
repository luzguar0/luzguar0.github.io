import random
for i in range(4):
    jugar=True
    cantidad=0
    vidas=10
    while(jugar):
      puerta= random.randint(1,3)
      #usuario elige la puerta
      a=int(input("¿Qué puerta elegis?"))

      print(puerta)
      if puerta== a:
        print("Ganaste")
        cantidad=cantidad+1
        jugar= False
      else:
        print("perdiste una vida")
        vidas=vidas-2
      if vidas==0:
        jugar=False
print("ganaste",cantidad,"veces")
