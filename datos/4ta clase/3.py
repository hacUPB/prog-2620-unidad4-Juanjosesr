def planificar_mantenimiento(aviones_mantenimiento, tecnicos_habilidades):
    """
    Asigna técnicos a tareas de mantenimiento de aeronaves basado en habilidades.
    """
    resultado = {}

    # Recorremos cada avión y sus tareas requeridas
    for avion, tareas in aviones_mantenimiento.items():
        resultado[avion] = {}  # creamos entrada para este avión

        # Recorremos cada técnico y sus habilidades
        for tecnico, habilidades in tecnicos_habilidades.items():

            # Vemos qué tareas del avión puede hacer este técnico
            puede_hacer = tareas & habilidades

            # Si puede hacer al menos una tarea, lo asignamos
            if len(puede_hacer) > 0:
                resultado[avion][tecnico] = puede_hacer

    return resultado

# Datos de prueba
mantenimiento_requerido = {
    "N12345": {"inspeccion-motor", "revision-hidraulica", "calibracion-instrumentos"},
    "N67890": {"revision-electrica", "inspeccion-combustible", "prueba-presion"},
    "N54321": {"inspeccion-motor", "revision-tren", "calibracion-instrumentos"},
    "N09876": {"revision-electrica", "revision-oxigeno", "actualizacion-software"}
}

habilidades_tecnicas = {
    "Técnico 1": {"inspeccion-motor", "revision-hidraulica", "revision-tren"},
    "Técnico 2": {"revision-electrica", "calibracion-instrumentos", "actualizacion-software"},
    "Técnico 3": {"inspeccion-combustible", "prueba-presion", "revision-oxigeno"},
    "Técnico 4": {"calibracion-instrumentos", "actualizacion-software", "inspeccion-motor"}
}

# Probando la función
plan = planificar_mantenimiento(mantenimiento_requerido, habilidades_tecnicas)
for avion, tecnicos in plan.items():
    print(f"\nAvión {avion}:")
    for tecnico, tareas in tecnicos.items():
        print(f"  {tecnico} puede hacer: {tareas}")