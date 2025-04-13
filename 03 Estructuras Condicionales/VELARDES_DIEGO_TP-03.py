from statistics import mode, median, mean
import random

# ACTIVIDADES

print("1.")

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    pass

print("2.")

nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

print("3.")

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("Por favor ingrese un número par")

print("4.")

edad = int(input("Ingrese su edad: "))
if edad < 0 and edad < 12:
    print("Pertenece a la categoría de Niño/a")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoría de Adolescente")
elif edad >= 18 and edad < 30:  
    print("Pertenece a la categoría Adulto/a joven") 
else:
    print("Pertenece a la categoría Adulto/a")

print("5.")

contraseña =  input("Ingrese la contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor ingrese una contraseña de entre 8 y 14 caracteres")


print("6.")

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("La moda es:", moda)
print("La mediana es:", mediana) 
print("La media es:", media)

if media > mediana and mediana > moda:
    print("La distribucion tiene sesgo positivo")
elif media < mediana and mediana < moda:
    print("La distribucion tiene sesgo negativo")
elif media == mediana and mediana == moda:
    print("La distribucion no tiene sego")


print("7.")

frase = input("Ingrese una frase o palabra: ").strip().lower()

if frase[-1] in "aeiou":
    frase += "!"
else:
    frase

print(frase)

print("8.")

nombre = input("Ingrese su nombre: ")
print("Ingrese una de las siguientes opciones:")
print("1. Si quiere su nombre en mayúsculas")
print("2. Si quiere su nombre en minúsculas")
print("3. Si quiere su nombre en capitalización")

eleccion = int(input("Ingrese su opción: "))
if eleccion == 1:
    print(nombre.upper())
elif eleccion == 2:
    print(nombre.lower())
elif eleccion == 3:
    print(nombre.capitalize())
else:
    pass

print("9.")

magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3.0:
    print("Muy leve")
elif 3.0 <= magnitud < 4.0:
    print("Leve")
elif 4.0 <= magnitud < 5.0:
    print("Moderado")
elif 5.0 <= magnitud < 6.0:
    print("Fuerte")
elif 6.0 <= magnitud < 7.0:
    print("Muy fuerte")
elif 7.0 <= magnitud:
    print("Extremo")

print("10.")

hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"La estación es: {estacion}")