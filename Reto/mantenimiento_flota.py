# RETO: Gestión de Mantenimiento de Flota Aeronáutica
# Estructuras usadas: listas y diccionarios
# Ciclos: for y while (sin list comprehensions)

# PASO 1: Registro de aeronaves
# Se crea una lista vacía que contendrá diccionarios,
# uno por cada aeronave ingresada por el usuario.
flota = []

print("=" * 50)
print("  SISTEMA DE MANTENIMIENTO DE FLOTA AERONÁUTICA")
print("=" * 50)

NUM_AERONAVES = 3  # Mínimo requerido por el enunciado

i = 0
while i < NUM_AERONAVES:
    print(f"\n  Aeronave {i + 1} de {NUM_AERONAVES}")

    matricula = input("Matrícula (ej. HK-4532): ")
    modelo    = input("Modelo   (ej. A320)    : ")

    # Validación básica: horas deben ser un número
    horas_validas = False
    while not horas_validas:
        horas_str = input("Horas de vuelo acumuladas: ")
        if horas_str.replace(".", "").isdigit():
            horas_vuelo = float(horas_str)
            horas_validas = True
        else:
            print("  ⚠ Ingresa un número válido.")

    # Cada aeronave es un diccionario con su información básica
    # y una lista vacía donde se añadirán sus componentes.
    aeronave = {
        "matricula":   matricula,
        "modelo":      modelo,
        "horas_vuelo": horas_vuelo,
        "componentes": []          # lista de diccionarios de componentes
    }

# PASO 2: Registro de componentes para esta aeronave
    print(f"\n  Registro de componentes para {matricula}")
    print("  (Escribe 'listo' como nombre para terminar)")

    while True:
        nombre_comp = input("\n  Nombre del componente: ")
        if nombre_comp.lower() == "listo":
            break

        # Validación horas de uso
        uso_valido = False
        while not uso_valido:
            uso_str = input("  Horas de uso actuales : ")
            if uso_str.replace(".", "").isdigit():
                horas_uso = float(uso_str)
                uso_valido = True
            else:
                print("  ⚠ Ingresa un número válido.")

        # Validación límite de horas
        limite_valido = False
        while not limite_valido:
            limite_str = input("  Límite de horas antes de mantenimiento: ")
            if limite_str.replace(".", "").isdigit():
                limite = float(limite_str)
                limite_valido = True
            else:
                print("  ⚠ Ingresa un número válido.")

        # Cada componente es un diccionario dentro de la lista
        # "componentes" de la aeronave correspondiente.
        componente = {
            "nombre":    nombre_comp,
            "horas_uso": horas_uso,
            "limite":    limite
        }

        aeronave["componentes"].append(componente)
        print(f"  ✔ Componente '{nombre_comp}' registrado.")

    # Añadir la aeronave completa a la flota
    flota.append(aeronave)
    i += 1

# PASO 3: Reporte de componentes que requieren
#         mantenimiento (horas_uso >= límite)
print("\n")
print("=" * 50)
print("        REPORTE DE MANTENIMIENTO INMEDIATO")
print("=" * 50)

hay_alertas = False  # bandera para saber si existe al menos una alerta

for aeronave in flota:
    for componente in aeronave["componentes"]:
        if componente["horas_uso"] >= componente["limite"]:
            if not hay_alertas:
                hay_alertas = True
            print(f"\n  ⚠ ALERTA - Aeronave : {aeronave['matricula']} ({aeronave['modelo']})")
            print(f"    Componente         : {componente['nombre']}")
            print(f"    Horas de uso       : {componente['horas_uso']}")
            print(f"    Límite permitido   : {componente['limite']}")
            exceso = componente["horas_uso"] - componente["limite"]
            print(f"    Exceso             : {exceso:.1f} h")

if not hay_alertas:
    print("\n  ✔ Todos los componentes están dentro de sus límites.")

print("\n" + "=" * 50)
print("  Aeronaves registradas en el sistema:", len(flota))
print("=" * 50)
