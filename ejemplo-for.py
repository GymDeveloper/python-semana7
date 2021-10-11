# range tiene la prpiedad de recibir 2 valores
# inical - final => final - 1
# for j in range(0, 101):
#     print("Numero: ", j)

for l in "Tecsup":
    # print("Letra: ", l)
    if l == "s":
        continue
    print("La le tra S funciona", l)

# Esto es un array de frutas
frutas = ['Pera', 'Manzana', 'Naranja', 'Papaya']

# for fruta in frutas:
#     print(fruta)
#     if fruta == "Naranja":
#         break

# print("El for se detuvo")
# 0...10
for number in range(11):
    if number % 2 == 0:
        pass  # sirve para decir que pase y no ejecuta nada
        print("Number", number)
