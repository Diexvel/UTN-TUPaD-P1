# Actividades de TP 5
# Ejercicio 1
print("******Ejercicio 1******")
lista_100 = list(range(4, 101, 4))
print(lista_100)

# Ejercicio 2
print("******Ejercicio 2******")

lista = ["river", "boca", "racing", "independiente", "velez"]
print("el penultimo elemento es:", lista[-2])

# Ejercicio 3
print("******Ejercicio 3******")

lista_vacia = []
lista_vacia.append("boca")
lista_vacia.append("river")
lista_vacia.append("racing")

print("la lista es:", lista_vacia)

# Ejercicio 4
print("******Ejercicio 4******")

animales = ["perro", "gato", "conejo","pez"]
animales[1] = "loro"
animales[3] = "oso"

print("la lista es:", animales)

# Ejercicio 5
print("******Ejercicio 5******")

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

print("El codigo enterior remueve el valor maximo encontrado en la lista numero, en este caso el 22")

# Ejercicio 6
print("******Ejercicio 6******")

lista = list(range(10, 31, 5))

print("los 2 primeros elementos son :", lista[:2])

# Ejercicio 7
print("******Ejercicio 7******")

autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "corsa"

print("la lista es:", autos)

# Ejercicio 8
print("******Ejercicio 8******")

dobles = []
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

# Ejercicio 9
print("******Ejercicio 9******")

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# A
compras[2].append("jugo")
# B
compras[1][1] = "tallarines"
# C
compras[0].remove("pan")
# D
print(compras)

# ejercicio 10
print("******Ejercicio 10******")

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)
