# Lista de vuelos: [destino, duración_min, precio_USD]
vuelos = [
    ["Bogotá",   55,  180],
    ["Medellín", 0,   0  ],  # origen
    ["Cali",     40,  120],
    ["Cartagena",75,  210],
    ["Leticia",  110, 340],
]

# 1. max() + len() — vuelo más largo
duraciones = [vuelos[i][1] for i in range(len(vuelos)) if vuelos[i][1] > 0]
max_dur = max(duraciones)              # 110

# 2. .index() — encontrar fila del vuelo más caro
precios  = [f[2] for f in vuelos]
idx_caro = precios.index(max(precios))  # 4 → Leticia

# 3. .pop() — eliminar origen de la lista
origen = vuelos.pop(1)                  # saca ["Medellín", 0, 0]

# 4. .append() — agregar vuelo nuevo
vuelos.append(["Barranquilla", 65, 195])