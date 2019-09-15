Veces = int(input("Dime cuantos nombres quieres que guarde: "))
contador = 1
listanombre = []
while contador <= Veces:
    nombre = input("Dame un nombre: ")
    contador = contador + 1
    listanombre = listanombre + [nombre] 
print (listanombre)

