componentes = ["alas", "fuselaje", "motores"]
print(id(componentes))  # Guardamos el ID original

# Modificamos la lista
componentes.append("tren de aterrizaje")
print(componentes)  # ["alas", "fuselaje", "motores", "tren de aterrizaje"]
print(id(componentes))  # Mismo ID, el objeto fue modificado in-place
