# actividades TP 05

# Deficion de funciones
# 1 
def imprimir_hola_mundo():
    print("Hola, mundo!")

# 2
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")

# 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#4
def calcular_area_circulo(radio):
    pi = 3.14159
    area = pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    perimetro = 2 * pi * radio
    return perimetro

#5
def segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas

#6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return suma, resta, multiplicacion, division

#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

#9
def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programa principal
#1
imprimir_hola_mundo()
#2
nombre_2 = input("Ingrese su nombre: ")
saludar_usuario(nombre_2)
#3
nombre_3 = input("Ingrese su nombre: ")
apellido_3 = input("Ingrese su apellido: ")
edad_3 = input("Ingrese su edad: ")
residencia_3 = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre_3, apellido_3, edad_3, residencia_3)

#4
radio_4 = float(input("Ingrese el radio del círculo: "))
area_4 = calcular_area_circulo(radio_4)
perimetro_4 = calcular_perimetro_circulo(radio_4)
print(f"El área del círculo es: {area_4}") 
print(f"El perímetro del círculo es: {perimetro_4}")

#5
segundos_5 = int(input("Ingrese la cantidad de segundos: "))
horas_5 = segundos_a_horas(segundos_5)
print(f"La cantidad de horas es: {horas_5}")

#6
numero_6 = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
tabla_multiplicar(numero_6)

#7
a_7 = int(input("Ingrese el primer número: "))
b_7 = int(input("Ingrese el segundo número: "))
suma_7, resta_7, multiplicacion_7, division_7 = operaciones_basicas(a_7, b_7)
print(f"Suma: {suma_7}")
print(f"Resta: {resta_7}")
print(f"Multiplicación: {multiplicacion_7}")
print(f"División: {division_7}")

#8
peso_8 = float(input("Ingrese su peso en kg: "))
altura_8 = float(input("Ingrese su altura en metros: "))
imc_8 = calcular_imc(peso_8, altura_8)
print(f"Su IMC es: {imc_8}")

#9
celsius_9 = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit_9 = celcius_a_fahrenheit(celsius_9)
print(f"La temperatura en Fahrenheit es: {fahrenheit_9}")

#10

a_10 = float(input("Ingrese el primer número: "))
b_10 = float(input("Ingrese el segundo número: "))  
c_10 = float(input("Ingrese el tercer número: "))
promedio_10 = calcular_promedio(a_10, b_10, c_10)
print(f"El promedio es: {promedio_10}")

# Fin del programa