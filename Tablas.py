#Melanie Arzola 16/09/2019
#For dentro de otro for permite mantener el programa hasta que termine
for i in range (1,11):
    titulo = ("Tabla del {}")
    print(titulo.format(i))
    print()
    for j in range(1,11):
        salida = ("{} x {} = {}")
        print(salida.format(i,j,i*j))
    else:
        print()
