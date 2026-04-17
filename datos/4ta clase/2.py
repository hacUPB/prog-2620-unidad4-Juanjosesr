def analizar_compatibilidad(componentes_por_modelo):
    """
    Analiza la compatibilidad de componentes entre modelos de aeronaves.

    Args:
        componentes_por_modelo: Diccionario donde las claves son modelos
                              y los valores son sets de componentes

    Returns:
        Diccionario con información de compatibilidad entre modelos
    """
    resultado = {}
    modelos = list(componentes_por_modelo.keys())

    for i in range(len(modelos)):
        for j in range(i + 1, len(modelos)):
            modelo1 = modelos[i]
            modelo2 = modelos[j]

            componentes1 = componentes_por_modelo[modelo1]
            componentes2 = componentes_por_modelo[modelo2]

            comparten = componentes1 & componentes2
            exclusivos1 = componentes1 - componentes2
            exclusivos2 = componentes2 - componentes1
            compatible = len(comparten) >= 2

            clave = f"{modelo1} - {modelo2}"
            resultado[clave] = {
                "comparten": comparten,
                "exclusivos_1": exclusivos1,
                "exclusivos_2": exclusivos2,
                "compatibles": compatible
            }

    return resultado

# Datos de prueba
componentes = {
    "B737-800": {"motor-CFM56", "apu-131-9B", "radar-WXR-2100", "fms-Pegasus", "transponder-Mode-S"},
    "B737-MAX": {"motor-LEAP-1B", "apu-131-9B", "radar-WXR-2100", "fms-Pegasus", "transponder-Mode-S"},
    "A320": {"motor-CFM56", "apu-APS3200", "radar-RDR-4000", "fms-Thales", "transponder-Mode-S"},
    "A320neo": {"motor-PW1100G", "apu-APS3200", "radar-RDR-4000", "fms-Thales", "transponder-Mode-S"}
}

# Probando la función
compatibilidad = analizar_compatibilidad(componentes)
for par, datos in compatibilidad.items():
    print(f"\n{par}")
    print(f"  Comparten: {datos['comparten']}")
    print(f"  Exclusivos modelo 1: {datos['exclusivos_1']}")
    print(f"  Exclusivos modelo 2: {datos['exclusivos_2']}")
    print(f"  Compatibles: {datos['compatibles']}")