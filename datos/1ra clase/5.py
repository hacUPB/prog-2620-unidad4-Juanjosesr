def agregar_combustible(tanques, litros):
    tanques.append(litros)
    print(f"Combustible actualizado: {tanques}")

combustible_actual = [1000, 1200, 800]  # Lista (objeto mutable)
agregar_combustible(combustible_actual, 500)
print(combustible_actual)  # [1000, 1200, 800, 500] - La lista original fue modificada