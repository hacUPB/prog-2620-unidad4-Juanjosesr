def analizar_perfil_ala(datos_tunel):
    """
    Analiza datos de pruebas de túnel de viento para diferentes perfiles de ala.

    Args:
        datos_tunel: Lista de tuplas con formato:
            (nombre_perfil, coef_sustentacion, coef_resistencia, angulo_ataque)

    Returns:
        Diccionario con análisis de los perfiles
    """
    resultados = {}

    for dato in datos_tunel:
        perfil = dato[0]
        cl = dato[1]
        cd = dato[2]
        angulo = dato[3]
        eficiencia = cl / cd  # razón de planeo

        # Si el perfil no está en el diccionario, lo agregamos
        if perfil not in resultados:
            resultados[perfil] = {
                "mejor_eficiencia": eficiencia,
                "angulo_mejor_eficiencia": angulo,
                "max_sustentacion": cl,
                "min_resistencia": cd
            }
        else:
            # Actualizamos si encontramos mejor eficiencia
            if eficiencia > resultados[perfil]["mejor_eficiencia"]:
                resultados[perfil]["mejor_eficiencia"] = eficiencia
                resultados[perfil]["angulo_mejor_eficiencia"] = angulo

            # Actualizamos si encontramos mayor sustentación
            if cl > resultados[perfil]["max_sustentacion"]:
                resultados[perfil]["max_sustentacion"] = cl

            # Actualizamos si encontramos menor resistencia
            if cd < resultados[perfil]["min_resistencia"]:
                resultados[perfil]["min_resistencia"] = cd

    return resultados

# Datos de prueba
datos_prueba = [
    ("NACA2412", 0.25, 0.021, 0),
    ("NACA2412", 0.45, 0.028, 2),
    ("NACA2412", 0.85, 0.036, 5),
    ("NACA4415", 0.32, 0.022, 0),
    ("NACA4415", 0.52, 0.029, 2),
    ("NACA4415", 0.95, 0.041, 5),
    ("NACA6412", 0.36, 0.028, 0),
    ("NACA6412", 0.62, 0.039, 2),
    ("NACA6412", 1.05, 0.065, 5)
]

# Probando la función
analisis = analizar_perfil_ala(datos_prueba)
for perfil, datos in analisis.items():
    print(f"\nPerfil: {perfil}")
    print(f"  Mejor eficiencia (CL/CD): {datos['mejor_eficiencia']:.2f}")
    print(f"  Ángulo de mejor eficiencia: {datos['angulo_mejor_eficiencia']}°")
    print(f"  Máxima sustentación: {datos['max_sustentacion']}")
    print(f"  Mínima resistencia: {datos['min_resistencia']}")