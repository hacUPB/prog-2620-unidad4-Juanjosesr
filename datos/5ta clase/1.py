def actualizar_horas_vuelo(flota, registro_vuelos):
    """
    Actualiza las horas de vuelo y ciclos de componentes basados en nuevos vuelos.
    """
    alertas = []

    # Recorremos cada vuelo registrado
    for vuelo in registro_vuelos:
        matricula = vuelo["matricula"]
        horas = vuelo["horas"]
        ciclos = vuelo["ciclos"]

        # Verificamos que la aeronave existe en la flota
        if matricula in flota:
            componentes = flota[matricula]["componentes"]

            # Actualizamos cada componente
            for nombre, datos in componentes.items():
                datos["horas_totales"] += horas
                datos["ciclos"] += ciclos

                # Verificamos límite de horas
                if "limite_horas" in datos:
                    if datos["horas_totales"] >= datos["limite_horas"]:
                        alertas.append(
                            f"ALERTA: {matricula} - {nombre} alcanzó límite de horas "
                            f"({datos['horas_totales']:.1f}/{datos['limite_horas']})"
                        )

                # Verificamos límite de ciclos
                if "limite_ciclos" in datos:
                    if datos["ciclos"] >= datos["limite_ciclos"]:
                        alertas.append(
                            f"ALERTA: {matricula} - {nombre} alcanzó límite de ciclos "
                            f"({datos['ciclos']}/{datos['limite_ciclos']})"
                        )

    return flota, alertas

# Datos de prueba
flota_aeronaves = {
    "N123AB": {
        "modelo": "Boeing 737-800",
        "componentes": {
            "motores": {"horas_totales": 12500, "ciclos": 4200, "limite_horas": 15000},
            "tren_aterrizaje": {"horas_totales": 10000, "ciclos": 4200, "limite_ciclos": 5000},
            "apu": {"horas_totales": 8500, "ciclos": 6300, "limite_horas": 10000}
        }
    },
    "N456CD": {
        "modelo": "Airbus A320",
        "componentes": {
            "motores": {"horas_totales": 18200, "ciclos": 7300, "limite_horas": 20000},
            "tren_aterrizaje": {"horas_totales": 15600, "ciclos": 7300, "limite_ciclos": 8000},
            "apu": {"horas_totales": 12400, "ciclos": 9100, "limite_horas": 15000}
        }
    }
}

vuelos_recientes = [
    {"matricula": "N123AB", "horas": 4.5, "ciclos": 2, "fecha": "2023-03-15"},
    {"matricula": "N456CD", "horas": 3.2, "ciclos": 1, "fecha": "2023-03-15"},
    {"matricula": "N123AB", "horas": 5.8, "ciclos": 2, "fecha": "2023-03-16"},
    {"matricula": "N456CD", "horas": 6.7, "ciclos": 3, "fecha": "2023-03-16"}
]

# Probando la función
flota_actualizada, alertas = actualizar_horas_vuelo(flota_aeronaves, vuelos_recientes)
print("Alertas de mantenimiento:")
for alerta in alertas:
    print(f"  {alerta}")