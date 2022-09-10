num=900
mult23=0
mult2=0
mult3=0

print("Ingrese el numero 0 para salir.")
while num != 0:
    num = int(input("Digite un numero entero: "))
    if num % 2 == 0 and num % 3 == 0:
        print(f"Multiplo de 2 y 3")
        print("")
        mult23 = mult23+1
    elif num % 2 == 0:
        print(f"Multiplo de 2")
        print("")
        mult2 = mult2+1
    elif num % 3 == 0:
        print(f"Multiplo de 3")
        print("")
        mult3 = mult3+1
    else:
        print(f"No es multiplo de 2 ni de 3")
        print("")
else:
    print(f"Se ingresaron {mult2} multiplos de 2. {mult3} multiplos de 3 y ademas {mult23} multiplos de 2 y 3.")
