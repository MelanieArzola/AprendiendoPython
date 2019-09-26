# Melanie Arzola 16/09/2019
#Pides el numero que quieren
tabla= int(input("Dame un numero del 1 al 9: "))

if tabla >9 or tabla <1:
    print("Este valor no es permitido")
else:
    for i in range(1,11):
        salida= "{} x {} = {}"
        print(salida.format(tabla,i,i*tabla))


