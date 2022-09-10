from math import prod


cent=100

#while
print("")
print("MENU")
print("1 - Crear producto")
print("2 - Mostrar productos")
print("3 - Buscar/Editar productos")
print("4 - Buscar/Eliminar")
print("0 - SALIR")

productos={}

while cent !=0:
    print("")
    cent=int(input("Elija una opcion entre 1 y 4: "))
    if cent == 1:
        productos["codigo"]=input("Codigo del producto: ")
        productos["nombre"]=input("Nombre del producto: ")
        productos["precio"]=input("Precio: $")
    elif cent == 2:
        print(productos)
    elif cent == 3:
        cod=input("Escriba el codigo del producto: ")
    elif cent == 0:
        break
else:
    print("Done!")