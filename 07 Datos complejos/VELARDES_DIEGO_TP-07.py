#Tp 7 Datos complejos
# Ejercicio 1
print("Ejercicio 1")

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadiendo nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Diccionario actualizado:")
print(precios_frutas)

# Ejercicio 2
print("\nEjercicio 2")

# Actualizando precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Diccionario con precios actualizados:")
print(precios_frutas)

# Ejercicio 3
print("\nEjercicio 3")

# Crear lista de nombres de frutas (claves del diccionario)
lista_frutas = list(precios_frutas.keys())

print("Lista de frutas:")
print(lista_frutas)

# Ejercicio 4
print("\nEjercicio 4")

# Crear diccionario vacío
agenda = {}

print("Cargá 5 contactos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

# Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés buscar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe en la agenda.")

# Ejercicio 5
print("\nEjercicio 5")

frase = input("Ingresá una frase: ").lower()
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Conteo de frecuencia
frecuencia = {}
for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de cada palabra:", frecuencia)

# Ejercicio 6
print("\nEjercicio 6")

alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Mostrar promedios
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

# Ejercicio 7
print("\nEjercicio 7")

parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {104, 105, 106, 107}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio 8
print("\nEjercicio 8")

stock = {"Pan": 10, "Leche": 20, "Huevos": 30}

producto = input("Ingresá el nombre de un producto: ")

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input(f"{producto} no existe. ¿Cuántas unidades querés agregar?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio 9
print("\nEjercicio 9")

agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "14:00"): "Clase de programación",
    ("viernes", "09:00"): "Entrega de informe"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

evento = agenda.get((dia, hora), "No hay actividad registrada en ese horario.")
print("Evento:", evento)

# Ejercicio 10
print("\nEjercicio 10")

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma"
}

capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario invertido:")
print(capitales)
