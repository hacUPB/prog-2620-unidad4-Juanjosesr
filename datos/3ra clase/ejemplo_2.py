# Waypoints definidos como tuplas (nombre, latitud, longitud, altitud mínima)
ruta_vuelo = [
    ("MADOW", 33.9425, -118.4081, 0),      # LAX departure
    ("SADDE", 34.3015, -118.4000, 7000),   # SoCal waypoint
    ("LRAIN", 36.2049, -115.1760, 19000),  # Near Las Vegas
    ("DNVER", 39.8561, -104.6737, 0)       # Denver arrival
]

# Cálculo de distancia aproximada de ruta
import math

def distancia_haversine(lat1, lon1, lat2, lon2):
    """Calcula la distancia en km entre dos puntos usando la fórmula de Haversine"""
    R = 6371  # Radio de la Tierra en km
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = (math.sin(dLat/2) * math.sin(dLat/2) +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(dLon/2) * math.sin(dLon/2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

distancia_total = 0
for i in range(len(ruta_vuelo) - 1):
    distancia_tramo = distancia_haversine(
        ruta_vuelo[i][1], ruta_vuelo[i][2],
        ruta_vuelo[i+1][1], ruta_vuelo[i+1][2]
    )
    distancia_total += distancia_tramo
    print(f"Tramo {ruta_vuelo[i][0]} a {ruta_vuelo[i+1][0]}: {distancia_tramo:.2f} km")

print(f"Distancia total del vuelo: {distancia_total:.2f} km")
