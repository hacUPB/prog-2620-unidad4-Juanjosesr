# Sets de aeronaves por aerolínea
flota_american = {"B737", "B777", "B787", "A320", "A321", "A330"}
flota_delta = {"B717", "B737", "B757", "B767", "A320", "A330", "A350"}
flota_united = {"B737", "B747", "B767", "B777", "B787", "A319", "A320"}

# Aeronaves comunes entre American y Delta
comunes_ad = flota_american.intersection(flota_delta)
print(f"Modelos operados por American y Delta: {comunes_ad}")

# Aeronaves operadas por al menos una de las tres aerolíneas
todas_aeronaves = flota_american.union(flota_delta, flota_united)
print(f"Total de modelos distintos: {len(todas_aeronaves)}")

# Aeronaves exclusivas de United (no operadas por las otras)
exclusivas_united = flota_united - flota_american - flota_delta
print(f"Modelos exclusivos de United: {exclusivas_united}")

# Aeronaves de American que no operan Delta
solo_american = flota_american - flota_delta
print(f"Modelos de American no operados por Delta: {solo_american}")
