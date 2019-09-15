def resultadotiempo (velocidadprimaria, distanciaprimaria):
    tiempocercano = distancia/velocidad
    return tiempocercano

velocidad = int(input("Dame una velocidad: "))
distancia = int(input("Ahora dame una distancia: "))
tiempo = resultadotiempo (velocidad, distancia)

print (tiempo)
