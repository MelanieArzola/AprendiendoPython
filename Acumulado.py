#Melanie Arzola 16/09/2019
acumulado = int(0)
numero= str("")
#While True funciona de tal forma que es un ciclo infinito hasta que un break lo termina
while True:
    numero = input("Dame un numero entero: ")
    if numero=="": #Si da un numero vacio, se detiene el programa
        print ("Vacío. Termina el programa")
        break
    else:
        #Suma incluyente (+-)
        acumulado+= int(numero)
        salida="Monto acumulado {}"
        print(salida.format(acumulado))
