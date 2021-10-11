# creo un acumlador que se encargue de la suma
suma = 0

for i in range(10):
    numero = int(input("Ingrese el numero " + str(i) + ": "))
    suma += numero

print("La suma es", suma)
