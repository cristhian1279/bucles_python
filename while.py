
puntaje =int(input("Ingrese número:"))
while True:
    if puntaje == 90:
        print("A")
    elif puntaje == 80:
        print("B")
    elif puntaje == 70:
        print("C")  
    elif puntaje == 60:
        print("D") 
    elif puntaje < 60:
        print("F")
    else:
        print("Vuelva a intentarlo!")
        break
    break    