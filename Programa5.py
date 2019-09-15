A = 50
B = 20
C = 28
intento = int(input("Dame un número: "))
while intento != A and intento != B and intento != C:
    intento = int(input("Intenta de nuevo: "))
    if intento == A or intento == B or intento == C:
        print ("Ha adivinado el número")
