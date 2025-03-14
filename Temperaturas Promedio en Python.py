def calcular_promedio_temperaturas(datos):
    """
    Calcula la temperatura promedio por ciudad a partir de datos organizados por semanas.

    Parámetros:
        datos (dict): Diccionario donde:
                       - Las claves son nombres de ciudades (str)
                       - Los valores son listas de listas con temperaturas de cada semana

    Retorna:
        dict: Diccionario con promedios de temperatura por ciudad
    """
    promedios = {}

    for ciudad, semanas in datos.items():
        total_temperatura = 0
        total_dias = 0

        # Sumar todas las temperaturas y contar días
        for semana in semanas:
            total_temperatura += sum(semana)
            total_dias += len(semana)

        # Calcular promedio evitando división por cero
        if total_dias == 0:
            promedios[ciudad] = 0.0
        else:
            promedios[ciudad] = round(total_temperatura / total_dias, 2)

    return promedios
# Datos de ejemplo para 3 ciudades durante 4 semanas
datos_temperaturas = {
    "Nueva York": [
        [70, 75, 72, 68],
        [68, 72, 75, 70],
        [65, 73, 70, 72],
        [72, 68, 75, 71]
    ],
    "Los Ángeles": [
        [85, 88, 90, 87],
        [87, 89, 92, 88],
        [84, 86, 89, 85],
        [86, 90, 91, 88]
    ],
    "Chicago": [
        [60, 62, 58, 65],
        [58, 61, 64, 59],
        [62, 59, 57, 63],
        [59, 64, 60, 62]
    ]
}

# Calcular promedios
resultados = calcular_promedio_temperaturas(datos_temperaturas)

# Mostrar resultados
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio}°F")