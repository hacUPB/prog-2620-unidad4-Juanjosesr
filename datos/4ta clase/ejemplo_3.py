# Certificaciones de pilotos
piloto1 = {"PPL", "IR", "MEP", "CPL"}  # Licencia privado, Instrumentos, Multimotor, Comercial
piloto2 = {"PPL", "IR", "CPL", "CFI", "CFII"}  # + Instructor, Instructor instrumentos
piloto3 = {"PPL", "IR", "CPL", "ATPL"}  # + Transporte de línea aérea

# Encontrar certificaciones comunes a todos los pilotos
comunes = piloto1.intersection(piloto2, piloto3)
print(f"Todos los pilotos tienen: {comunes}")

# Certificaciones que tiene al menos uno
todas_cert = piloto1.union(piloto2, piloto3)
print(f"Total de certificaciones distintas: {todas_cert}")

# Certificaciones únicas de cada piloto
unicas_p1 = piloto1 - piloto2 - piloto3
unicas_p2 = piloto2 - piloto1 - piloto3
unicas_p3 = piloto3 - piloto1 - piloto2

print(f"Únicas del piloto 1: {unicas_p1}")
print(f"Únicas del piloto 2: {unicas_p2}")
print(f"Únicas del piloto 3: {unicas_p3}")

# Verificar si un piloto puede ser instructor
if {"CFI", "CFII"}.issubset(piloto2):
    print("El piloto 2 puede ser instructor de vuelo por instrumentos")