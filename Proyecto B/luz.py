vidas = int(input("ingrese cantidad de vidas"))
if vidas>=5:
    print("El nivel es fácil")
else:
    if vidas<=4:
        if vidas<=2:
         print("El nivel es dificil")
        else:
          print("El nivel es medio")
