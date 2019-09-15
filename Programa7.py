veces = int(input("¿Cuantas palabras tiene tu frase: "))
contador = 1
listapalabras = ""
while contador <= veces:
    palabras = input("Dame la palabra: ")
    listapalabras = listapalabras + palabras
    contador = contador + 1
palindromo = listapalabras [::-1]
print (listapalabras)
if listapalabras == palindromo:
    print ("Esta palabra es un palindromo")
else:
    print ("Esta palabra no es un palindromo")