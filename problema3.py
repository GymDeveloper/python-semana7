# PIDE N numeros
# tenemos que crear una variable limite
limite = int(input("Ingres el limite: "))

suma = 0

for i in range(1, limite, 2):
    number = int(input("Ingre el numero: "))
    suma += number
    # aca falta la suma

# el promedio
promedio = suma / limite
print("La suma es ", suma)
print("El primedio es ", promedio)
