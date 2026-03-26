lista = [1, 3, 4]
print(f"lista sin insert: {lista}")

lista.insert(1, 2)
print(f"lista con insert: {lista}")

lista.insert(len(lista), 8)
print(f"lista con insert(len(...)): {lista} ")