# Registro de mantenimiento: piezas reemplazadas en diferentes inspecciones
inspeccion_100h = {"filtro-aceite", "filtro-combustible", "bujías", "correa-alternador"}
inspeccion_500h = {"filtro-aceite", "filtro-combustible", "bujías", "bomba-combustible",
                  "mangueras-hidraulicas", "fluido-hidraulico"}
inspeccion_1000h = {"filtro-aceite", "filtro-combustible", "bujías", "bomba-combustible",
                   "mangueras-hidraulicas", "fluido-hidraulico", "tren-aterrizaje",
                   "sistema-frenos", "sistema-presurización"}

# Piezas que solo se reemplazan en la inspección de 1000h
solo_1000h = inspeccion_1000h - inspeccion_500h - inspeccion_100h
print(f"Piezas exclusivas de la inspección de 1000h: {solo_1000h}")

# ¿Las piezas de 500h incluyen todas las de 100h?
if inspeccion_100h.issubset(inspeccion_500h):
    print("La inspección de 500h incluye todas las piezas de la de 100h")
else:
    print("Hay piezas en la inspección de 100h que no están en la de 500h")

# Total de piezas únicas en todas las inspecciones
todas_piezas = inspeccion_100h | inspeccion_500h | inspeccion_1000h
print(f"Total de piezas diferentes a revisar: {len(todas_piezas)}")