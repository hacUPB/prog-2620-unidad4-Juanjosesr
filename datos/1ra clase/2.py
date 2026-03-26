velocidad = 800  # km/h
print(id(velocidad))  # Muestra el identificador único del objeto

otra_velocidad = 800
print(id(otra_velocidad))  # Para números pequeños, Python reutiliza objetos

lista1 = [1, 3, 67]
print(id(lista1))