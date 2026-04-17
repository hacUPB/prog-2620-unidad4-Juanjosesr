# Datos meteorológicos para diferentes aeropuertos
meteo = {
    "KLAX": {"temp": 22, "viento": 10, "direccion": 270, "visibilidad": 10000},
    "KJFK": {"temp": 15, "viento": 15, "direccion": 180, "visibilidad": 8000},
    "KORD": {"temp": 5, "viento": 25, "direccion": 320, "visibilidad": 5000}
}

# Añadir un nuevo aeropuerto con setdefault
meteo.setdefault("KMIA", {"temp": 28, "viento": 8, "direccion": 90, "visibilidad": 9000})

# Actualizar datos existentes con update
meteo["KORD"].update({"temp": 3, "visibilidad": 3000, "precipitacion": "nieve"})

# Crear copia y hacer modificaciones
meteo_actualizado = meteo.copy()
for aeropuerto in meteo_actualizado:
    # Convertir temperatura de Celsius a Fahrenheit
    meteo_actualizado[aeropuerto]["temp_F"] = round(meteo_actualizado[aeropuerto]["temp"] * 9/5 + 32, 1)

    # Categorizar visibilidad
    if meteo_actualizado[aeropuerto]["visibilidad"] < 5000:
        meteo_actualizado[aeropuerto]["categoria"] = "IMC"  # Instrumental Meteorological Conditions
    else:
        meteo_actualizado[aeropuerto]["categoria"] = "VMC"  # Visual Meteorological Conditions

# Mostrar datos actualizados
for aeropuerto, datos in meteo_actualizado.items():
    print(f"\\nAeropuerto: {aeropuerto}")
    for parametro, valor in datos.items():
        print(f"  {parametro}: {valor}")