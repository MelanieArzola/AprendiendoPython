#Melanie Arzola 16/09/2019
numero=int(input("Dame un número entero: "))

Multiplo3=((numero%3)==0)
Multiplo5=((numero%5)==0)
Multiplo7=((numero%7)==0)
#Estas 3 variables guardaran valores booleanos, si el
#residuo es 0, querra decir que es múltiplo.

if ((Multiplo3 and Multiplo5) or Multiplo7):
    print("Correcto")
else:
    print("Incorrecto")