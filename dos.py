cent=0
frutas={}

while cent<10:
    if cent<10:
        frutas["fruta1"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta2"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta3"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta4"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta5"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta6"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta7"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta8"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta9"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1

        frutas["fruta10"]=input("Agregue el nombre de una fruta: ")
        cent = cent+1
else:
    res = dict(reversed(list(frutas.items())))
    
    res = {v: k for k, v in res.items()}
    for re in res:
        print(re)