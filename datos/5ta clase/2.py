def analizar_rendimiento(datos_vuelo, especificaciones):
    """
    Analiza el rendimiento de una aeronave comparando datos de vuelo
    con especificaciones del fabricante.
    """
    analisis = {}

    # Comparamos consumo real vs óptimo
    analisis["consumo"] = {}
    for fase, niveles in datos_vuelo["consumo"].items():
        analisis["consumo"][fase] = {}
        for nivel, valor_real in niveles.items():
            valor_optimo = especificaciones["consumo_optimo"][fase][nivel]
            diferencia = valor_real - valor_optimo
            porcentaje = (diferencia / valor_optimo) * 100
            analisis["consumo"][fase][nivel] = {
                "real": valor_real,
                "optimo": valor_optimo,
                "diferencia": diferencia,
                "porcentaje": round(porcentaje, 2),
                "recomendacion": "Revisar eficiencia" if porcentaje > 5 else "Normal"
            }

    # Comparamos velocidades reales vs óptimas
    analisis["velocidades"] = {}
    for fase, niveles in datos_vuelo["velocidades"].items():
        analisis["velocidades"][fase] = {}
        for nivel, valor_real in niveles.items():
            valor_optimo = especificaciones["velocidades_optimas"][fase][nivel]
            diferencia = valor_real - valor_optimo
            porcentaje = (diferencia / valor_optimo) * 100
            analisis["velocidades"][fase][nivel] = {
                "real": valor_real,
                "optimo": valor_optimo,
                "diferencia": diferencia,
                "porcentaje": round(porcentaje, 2),
                "recomendacion": "Ajustar velocidad" if abs(porcentaje) > 3 else "Normal"
            }

    return analisis

# Datos de prueba
especificaciones_b737 = {
    "consumo_optimo": {
        "crucero": {"FL290": 2200, "FL330": 2100, "FL370": 2050},
        "ascenso": {"inicial": 3100, "medio": 2800, "final": 2500},
        "descenso": {"inicial": 1800, "medio": 1500, "final": 1200}
    },
    "velocidades_optimas": {
        "crucero": {"FL290": 450, "FL330": 460, "FL370": 470},
        "ascenso": {"inicial": 290, "medio": 280, "final": 270},
        "descenso": {"inicial": 280, "medio": 270, "final": 250}
    }
}

datos_operacionales = {
    "vuelo_123": {
        "consumo": {
            "crucero": {"FL290": 2350, "FL330": 2150, "FL370": 2080},
            "ascenso": {"inicial": 3300, "medio": 2950, "final": 2600},
            "descenso": {"inicial": 1850, "medio": 1600, "final": 1300}
        },
        "velocidades": {
            "crucero": {"FL290": 440, "FL330": 455, "FL370": 465},
            "ascenso": {"inicial": 280, "medio": 270, "final": 260},
            "descenso": {"inicial": 290, "medio": 280, "final": 260}
        }
    }
}

# Probando la función
analisis = analizar_rendimiento(datos_operacionales["vuelo_123"], especificaciones_b737)
print("Análisis de rendimiento:")
for categoria, datos in analisis.items():
    print(f"\n{categoria.upper()}:")
    for subcategoria, valores in datos.items():
        print(f"  {subcategoria}: {valores}")