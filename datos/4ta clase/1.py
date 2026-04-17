def analizar_rutas(aerolineas_rutas):
    """
    Analiza las rutas de diferentes aerolíneas para identificar
    posibles alianzas estratégicas.
    """
    resultado = {}
    nombres = list(aerolineas_rutas.keys())  # ["Aerolínea A", "Aerolínea B", "Aerolínea C"]

    # Comparamos cada par de aerolíneas
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            aerolinea1 = nombres[i]
            aerolinea2 = nombres[j]

            rutas1 = aerolineas_rutas[aerolinea1]
            rutas2 = aerolineas_rutas[aerolinea2]

            # Rutas en común
            comunes = rutas1 & rutas2

            # Guardamos el análisis
            clave = f"{aerolinea1} - {aerolinea2}"
            resultado[clave] = {
                "rutas_comunes": comunes,
                "total_comunes": len(comunes),
                "alianza_recomendada": len(comunes) >= 2
            }

    return resultado

# Datos de prueba
rutas = {
    "Aerolínea A": {"LAX-JFK", "LAX-ORD", "ORD-JFK", "JFK-LHR", "LAX-NRT", "JFK-CDG"},
    "Aerolínea B": {"LAX-ORD", "ORD-JFK", "JFK-FRA", "FRA-CDG", "LAX-SYD", "SYD-NRT"},
    "Aerolínea C": {"MEX-LAX", "MEX-JFK", "MEX-BOG", "BOG-GRU", "MEX-MAD", "MAD-CDG"}
}

# Probando la función
analisis = analizar_rutas(rutas)
for par, datos in analisis.items():
    print(f"\n{par}")
    print(f"  Rutas en común: {datos['rutas_comunes']}")
    print(f"  Total comunes: {datos['total_comunes']}")
    print(f"  Alianza recomendada: {datos['alianza_recomendada']}")