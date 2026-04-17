def simular_costos(rutas, aeronaves, precios_combustible, tarifas_aeroportuarias):
    """
    Simula los costos operativos de diferentes combinaciones de rutas y aeronaves.
    """
    resultado = {}

    for nombre_ruta, datos_ruta in rutas.items():
        resultado[nombre_ruta] = {}
        origen = datos_ruta["origen"]
        destino = datos_ruta["destino"]
        tiempo = datos_ruta["tiempo_estimado"]

        for nombre_aeronave, datos_aeronave in aeronaves.items():
            # Costo de combustible
            consumo_total = datos_aeronave["consumo"] * tiempo
            precio_combustible = precios_combustible.get(origen, 0)
            costo_combustible = consumo_total * precio_combustible

            # Costo de tripulación
            costo_tripulacion = datos_aeronave["costos_tripulacion"] * tiempo

            # Tarifas aeroportuarias
            tarifa_origen = tarifas_aeroportuarias.get(origen, 0)
            tarifa_destino = tarifas_aeroportuarias.get(destino, 0)
            costo_aeroportuario = tarifa_origen + tarifa_destino

            # Costo total
            costo_total = costo_combustible + costo_tripulacion + costo_aeroportuario

            # Costo por pasajero
            costo_por_pax = costo_total / datos_aeronave["capacidad_pax"]

            resultado[nombre_ruta][nombre_aeronave] = {
                "costo_combustible": round(costo_combustible, 2),
                "costo_tripulacion": round(costo_tripulacion, 2),
                "costo_aeroportuario": round(costo_aeroportuario, 2),
                "costo_total": round(costo_total, 2),
                "costo_por_pax": round(costo_por_pax, 2)
            }

    return resultado

# Datos de prueba
rutas_ejemplo = {
    "LAX-JFK": {"distancia": 3983, "tiempo_estimado": 5.5, "origen": "LAX", "destino": "JFK"},
    "JFK-LHR": {"distancia": 5541, "tiempo_estimado": 7.0, "origen": "JFK", "destino": "LHR"},
    "LAX-NRT": {"distancia": 8773, "tiempo_estimado": 11.5, "origen": "LAX", "destino": "NRT"}
}

aeronaves_ejemplo = {
    "B737-800": {
        "capacidad_pax": 162,
        "consumo": 2600,
        "velocidad_crucero": 840,
        "costos_tripulacion": 1200
    },
    "B777-300ER": {
        "capacidad_pax": 396,
        "consumo": 7200,
        "velocidad_crucero": 905,
        "costos_tripulacion": 2100
    },
    "A320neo": {
        "capacidad_pax": 165,
        "consumo": 2400,
        "velocidad_crucero": 833,
        "costos_tripulacion": 1150
    }
}

precios_combustible = {
    "LAX": 0.85,
    "JFK": 0.92,
    "LHR": 1.10,
    "NRT": 1.05
}

tarifas_aeroportuarias = {
    "LAX": 3200,
    "JFK": 4100,
    "LHR": 5800,
    "NRT": 4900
}

# Probando la función
costos = simular_costos(rutas_ejemplo, aeronaves_ejemplo, precios_combustible, tarifas_aeroportuarias)
for ruta, aeronaves in costos.items():
    print(f"\nRuta: {ruta}")
    for aeronave, datos in aeronaves.items():
        print(f"  {aeronave}:")
        for concepto, valor in datos.items():
            print(f"    {concepto}: ${valor:,.2f}")