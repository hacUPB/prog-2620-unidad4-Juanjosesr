def comparar_rendimiento(aeronaves):
    """
    Analiza el rendimiento de diferentes aeronaves basado en sus características.

    Args:
        aeronaves: Lista de tuplas con formato:
            (nombre, consumo_combustible, velocidad_crucero, capacidad_carga)
            donde consumo está en L/km, velocidad en km/h y carga en kg

    Returns:
        Tupla con (aeronave_más_eficiente, aeronave_más_rápida, aeronave_mayor_capacidad)
    """
    # Inicializamos los récords
    mejor_eficiencia_valor = float('inf')  # buscamos el MENOR consumo
    mejor_eficiencia = None
    
    mayor_velocidad_valor = 0              # buscamos el MAYOR
    mas_rapida = None
    
    mayor_capacidad_valor = 0             # buscamos el MAYOR
    mayor_capacidad = None

    for avion in aeronaves:
        
        # Más eficiente → índice [1], el menor consumo
        if avion[1] < mejor_eficiencia_valor:
            mejor_eficiencia_valor = avion[1]
            mejor_eficiencia = avion

        # Más rápida → índice [2], la mayor velocidad
        if avion[2] > mayor_velocidad_valor:
            mayor_velocidad_valor = avion[2]
            mas_rapida = avion

        # Mayor capacidad → índice [3], la mayor carga
        if avion[3] > mayor_capacidad_valor:
            mayor_capacidad_valor = avion[3]
            mayor_capacidad = avion

    return (mejor_eficiencia, mas_rapida, mayor_capacidad)

# Datos de prueba (nombre, consumo L/km, velocidad km/h, carga kg)
aviones = [
    ("Boeing 747-8F", 12.5, 908, 134200),
    ("Airbus A330-200F", 8.0, 871, 70000),
    ("Boeing 777F", 7.2, 896, 103000),
    ("Antonov An-124", 15.6, 800, 150000)
]

# Probando la función
mejor_eficiencia, mas_rapido, mayor_carga = comparar_rendimiento(aviones)
print(f"Más eficiente: {mejor_eficiencia}")
print(f"Más rápido: {mas_rapido}")
print(f"Mayor capacidad: {mayor_carga}")