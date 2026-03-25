lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"lista original: {lista}")

lista.remove(1)
print(f"lista con remove: {lista}")

lista.remove(10)
print(f"lista con remove que no existe: {lista}")