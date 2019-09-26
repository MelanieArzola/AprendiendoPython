# Melanie Arzola 16/09/2019
numero1=int(input("Dame un primer numero: "))
numero2=int(input("Dame un segundo numero: "))

if numero1 > numero2:
    salida1= ("Numeros proporcionados {} y {}. El mayor es el primero")
    print(salida1.format(numero1,numero2))
elif numero2>numero1:
    salida2=("Numeros proporcionados {} y {}. El mayor es el segundo")
    print(salida2.format(numero1,numero2))
else:
    salida3=("Numeros proporcionados {} y {}. Los dos numeros son iguales")
    print(salida3.format(numero1,numero2))