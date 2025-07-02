## Tp de Recursividad

## ejercicio 1
print("Ejercicio 1: Factoriales")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Solicita un número al usuario
limite = int(input("Ingrese un número entero positivo: "))

# Muestra todos los factoriales desde 1 hasta el número ingresado
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

## ejercicio 2
print("\nEjercicio 2: Fibonacci")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Solicita al usuario la cantidad de términos
limite = int(input("¿Cuántos términos de Fibonacci querés ver?: "))

# Imprime la serie completa
for i in range(limite):
    print(f"F({i}) = {fibonacci(i)}")

## ejercicio 3
print("\nEjercicio 3: Potencia recursiva")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Prueba general
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

print(f"{base}^{exponente} = {potencia(base, exponente)}")

## ejercicio 4
print("\nEjercicio 4: Conversión de decimal a binario")

def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número entero positivo: "))

# Caso especial si el número es 0
if numero == 0:
    print("Binario: 0")
else:
    print(f"Binario: {decimal_a_binario(numero)}")


## ejercicio 5
print("\nEjercicio 5: Suma de dígitos")

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo
print(es_palindromo("reconocer"))  # True
print(es_palindromo("hola"))       # False

## ejercicio 6
print("\nEjercicio 6: Suma de dígitos")

def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# Ejemplos
print(suma_digitos(1234))  # 10
print(suma_digitos(9))     # 9
print(suma_digitos(305))   # 8

## ejercicio 7
print("\nEjercicio 7: Contar bloques")

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplos
print(contar_bloques(1))  # 1
print(contar_bloques(2))  # 3
print(contar_bloques(4))  # 10

## ejercicio 8
print("\nEjercicio 8: Contar dígitos específicos")

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    if ultimo == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Ejemplos
print(contar_digito(12233421, 2))  # 3
print(contar_digito(5555, 5))      # 4
print(contar_digito(123456, 7))    # 0

