a = 0
b = 1
n = int(input("Ingrese el límite: "))
suma = 0
for number in range(n):
    c = a+b
    a = b
    b = c
    print(b, end=", ")
    suma += b

print("La suma es", suma)
