def optimizar_ruta(origen, destino, waypoints, condiciones_clima):
    """
    Determina la mejor ruta considerando distancia y clima.

    Args:
        origen: Tupla (nombre, latitud, longitud)
        destino: Tupla (nombre, latitud, longitud)
        waypoints: Lista de tuplas (nombre, latitud, longitud)
        condiciones_clima: Diccionario con claves = nombres de waypoints
                          valores = índice de riesgo climático (0-10)

    Returns:
        Lista de tuplas con la ruta óptima incluyendo origen y destino
    """
    # Empezamos la ruta con el origen
    ruta_optima = [origen]
    
    # Revisamos cada waypoint intermedio
    for waypoint in waypoints:
        nombre = waypoint[0]
        
        # Solo incluimos el waypoint si el riesgo climático es <= 5
        if condiciones_clima[nombre] <= 5:
            ruta_optima.append(waypoint)
    
    # Agregamos el destino al final
    ruta_optima.append(destino)
    
    return ruta_optima

# Datos de prueba
origen = ("KLAX", 33.9425, -118.4081)
destino = ("KJFK", 40.6413, -73.7781)
puntos_intermedios = [
    ("KDEN", 39.8561, -104.6737),
    ("KORD", 41.9742, -87.9073),
    ("KCLE", 41.4075, -81.8511),
    ("KBNA", 36.1245, -86.6782)
]
clima = {"KDEN": 2, "KORD": 8, "KCLE": 5, "KBNA": 3}

# Probando la función
mejor_ruta = optimizar_ruta(origen, destino, puntos_intermedios, clima)
print("Ruta óptima:")
for punto in mejor_ruta:
    print(f"  {punto[0]} ({punto[1]}, {punto[2]})")