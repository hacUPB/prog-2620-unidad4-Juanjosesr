# Agregado al código original
componentes = ["alas", "fuselaje", "motores", "tren de aterrizaje"]

# Indexación (comienza en 0)
print(componentes[0])  # "alas"
print(componentes[-1])  # "tren de aterrizaje" (indexación negativa)

# Slicing (rebanado)
print(componentes[1:3])  # ["fuselaje", "motores"]
print(componentes[:2])   # ["alas", "fuselaje"]
print(componentes[2:])   # ["motores", "tren de aterrizaje"]

# ¿Qué sucede si accedo a un índice negativo?
# Python permite índices negativos para recorrer la lista desde el final hacia el inicio


# ¿Cuántas "vueltas" puedo darle con índices negativos?
# Solo una vuelta. Los índices negativos válidos van desde -1 hasta el número negativo de la cantidad que hay en la lista, que en este caso es -4.


# ¿Para qué sirven los dos puntos : dentro de los corchetes?
# Sirven para hacer slicing (rebanado), es decir, extraer una porción de la lista. La sintaxis es:
# lista[inicio:fin]  # desde inicio hasta fin (sin incluir fin)