Numero = int(input("Dame un número por favor: "))
if Numero >= 1 and Numero <= 100:
    print ("Su número esta en el rango de 1 a 100")
elif Numero <= 0:
    print ("Su número es menor a 0")
else:
    print ("Su número es mayor a 100")