import random

# Actividades

print("Ejercicio 1")

for i in range(0, 101):
    print(i) 

print("Ejercicio 2")

numero = int(input("Ingrese un número: "))
digitos = 0

while numero > 0:
    numero = numero // 10
    digitos += 1

print("El número tiene", digitos, "dígitos")

print("Ejercicio 3")

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
sumatoria = 0

if numero_1 > numero_2:
    for i in range(numero_2 + 1, numero_1):
        sumatoria += i
else:
    for i in range(numero_1 + 1, numero_2):
        sumatoria += i

if numero_1 == numero_2:
    print("Los números son iguales")    


print("La sumatoria de los números entre", numero_1, "y", numero_2, " excluyendo estos valores es:", sumatoria)

print("Ejercicio 4")

numero = int(input("Ingrese un número: "))
acumulador = 0

while numero != 0:
    acumulador += numero
    numero = int(input("Ingrese un número: "))

print("La sumatoria de los números ingresados es:", acumulador)

print("Ejercicio 5")

numero_aleatorio = random.randint(0, 9)
intentos = 0
numero = int(input("Adivine el número entre 0 y 9: "))

while numero != numero_aleatorio:
    intentos += 1
    numero = int(input("Incorrecto. Adivine el número entre 0 y 9: "))

print("¡Correcto! Adivinaste el número en", intentos, "intentos. El número era:", numero_aleatorio)

print("Ejercicio 6")

for i in range(100,0,-1):
    if i % 2 == 0:
        print(i)

print("Ejercicio 7")

numero = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(1, numero + 1):
    suma += i

print("La suma de los números desde 1 hasta", numero, "es:", suma)

print("Ejercicio 8")

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(10):
   numero = int(input("introduzca un numero: "))
   if numero % 2 == 0:
        pares += 1
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
   else:
        impares += 1
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1

print("pares: ", pares)
print("impares: ", impares)
print("positivos: ", positivos)
print("negativos: ", negativos)
print("total: ", pares + impares)

print("Ejercicio 9")

total = 0
cantidad = 0

for i in range(10):
    numero = int(input("ingrese numeros: "))
    total += numero
    cantidad += 1

print("La media de los numeros es: ", total / cantidad)


print("Ejercicio 10")

numero = int(input("Ingresá un número: "))
es_negativo = numero < 0
numero = abs(numero)

invertido = 0
while numero != 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero //= 10

if es_negativo:
    invertido *= -1

print(f"Número invertido: {invertido}")



