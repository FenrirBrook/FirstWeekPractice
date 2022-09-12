print("1:Lunes\n2:Martes\n3:Domingo")
opcion = int(input("Escoge un dia: "))

try:
    if opcion == 1:
        print("hoy trabajas")
    elif opcion == 2:
        print("hoy tienes una cena")
    elif opcion == 3:
        print("hoy descansas")
    else:
        print("Opcion no valida")
except:
    print("Digite un numero del menu")
