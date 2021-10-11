# contador = 0

# while True:
#     print("Tecsup", contador)
#     contador += 1

# numeros pares

# contador = 0

# while contador < 10:
#     if contador % 2 == 0:
#         print("Numero par", contador)
#     # contador = contador + 1
#     contador += 1

# Bucles anidados
# Realice un bucle que imprima la tabla del 1 al 12

# Creo un for para los numeros 1...12 Esto se repite 12
for number in range(1, 13):
    # Creo un for para los numeros 1...12 Esto se repite 12
    for mul in range(1, 13):
        # number = 2
        # mul = 1...12
        operation = number * mul
        print(str(number) + " * " + str(mul) + " = " + str(operation))
    print("-"*30)
