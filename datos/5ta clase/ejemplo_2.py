# Rendimiento de aeronave en diferentes condiciones
rendimiento_b737 = {
    "nivel_mar": {
        "velocidad_despegue": 250,  # km/h
        "distancia_despegue": 2300,  # metros
        "velocidad_ascenso": 550,  # km/h
        "regimen_ascenso": 700  # pies/minuto
    },
    "altitud_media": {  # 5000 pies
        "velocidad_despegue": 260,
        "distancia_despegue": 2600,
        "velocidad_ascenso": 520,
        "regimen_ascenso": 650
    },
    "altitud_alta": {  # 10000 pies
        "velocidad_despegue": 270,
        "distancia_despegue": 3200,
        "velocidad_ascenso": 500,
        "regimen_ascenso": 550
    }
}

# Calcular penalización porcentual por altitud
def calcular_penalizacion(condiciones, referencia="nivel_mar"):
    """Calcula la penalización porcentual en rendimiento debido a la altitud"""
    resultados = {}
    condicion_base = rendimiento_b737[referencia]
    condicion_comparada = rendimiento_b737[condiciones]

    for parametro in condicion_base:
        base = condicion_base[parametro]
        comparado = condicion_comparada[parametro]

        # Para distancia, mayor es peor; para el resto, menor es peor
        if parametro == "distancia_despegue":
            penalizacion = (comparado - base) / base * 100
        else:
            penalizacion = (base - comparado) / base * 100

        resultados[parametro] = round(penalizacion, 1)

    return resultados

# Calcular penalizaciones
penalizacion_alta = calcular_penalizacion("altitud_alta")
print("\\nPenalización por operar en altitud alta (%):")
for parametro, valor in penalizacion_alta.items():
    print(f"  {parametro}: {valor}%")