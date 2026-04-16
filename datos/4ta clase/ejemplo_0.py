# Set vacío (requiere constructor set())
aeropuertos = set()

# Set con elementos
aeropuertos = {"KLAX", "KJFK", "KORD", "KDEN", "KATL"}

# Crear set a partir de otra colección
codigos_IATA = set(["LAX", "JFK", "ORD", "DEN", "ATL"])

# Set para eliminar duplicados
vuelos_diarios = set(["AA123", "DL456", "UA789", "AA123", "DL456"])
print(vuelos_diarios)  # {'AA123', 'DL456', 'UA789'} (elimina duplicados)



# Añadir elemento
aeropuertos.add("KSEA")  # Añade Seattle

# Eliminar elemento
aeropuertos.remove("KORD")  # Elimina Chicago (genera error si no existe)
aeropuertos.discard("KMIA")  # Intenta eliminar Miami (no genera error si no existe)

# Comprobar pertenencia
if "KLAX" in aeropuertos:
    print("Los Angeles está en la lista")

# Longitud
print(f"Total de aeropuertos: {len(aeropuertos)}")