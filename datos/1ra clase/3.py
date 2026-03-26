modelo = "Boeing 747"
print(id(modelo))  # Guardamos el ID original

# Intentamos "modificar" el string
modelo = modelo + "-800"
print(modelo)  # "Boeing 747-800"
print(id(modelo))  # ¡ID diferente! Se creó un nuevo objeto