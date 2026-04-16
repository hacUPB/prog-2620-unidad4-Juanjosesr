# Tupla de sensores con sus valores
lecturas_sensor = (1013.25, 22.5, 65.3, 12.2)  # presión, temp, humedad, viento

# Longitud de la tupla
print(f"Número de sensores: {len(lecturas_sensor)}")

# Valor máximo y mínimo
print(f"Lectura máxima: {max(lecturas_sensor)}")
print(f"Lectura mínima: {min(lecturas_sensor)}")

# Conversión entre tuplas y listas
lista_sensores = list(lecturas_sensor)
lista_sensores.append(98.6)  # Añadir un valor (solo posible en listas)
nuevas_lecturas = tuple(lista_sensores)  # Convertir de nuevo a tupla
print(nuevas_lecturas)