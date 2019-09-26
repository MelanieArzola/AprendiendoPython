# Melanie Arzola 16/09/2019
import random

decimal = (float("28.20"))

def Decimales():
    decimal2 = float(random.randrange(1,10))

    mensaje= ("La suma de ¨{} y {} es {}")
    print(mensaje.format(decimal,decimal2, decimal+decimal2))
Decimales()