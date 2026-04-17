vuelo = {
    "aerolinea": "Avianca",
    "vuelo": "AV123",
    "origen": "BOG",
    "destino": "MDE"
}

#ejercicio 2 
ciudad_llegada = vuelo["destino"]
print(ciudad_llegada)

#ejercicio 3
vuelo["destino"] = "CLO"
print(vuelo)

#ejercicio 4
vuelo["estado"] = "En el aire"
print(vuelo)

#ejercicio 5
print(vuelo.get("piloto", "Piloto no asignado"))

#ejercicio 6
vuelo.pop("vuelo")
print(vuelo)