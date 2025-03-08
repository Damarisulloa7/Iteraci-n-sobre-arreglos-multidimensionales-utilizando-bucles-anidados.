import random

# 1. Crear matriz 3D con datos de ejemplo
ciudades = ["Nueva York", "Los Ángeles", "Chicago"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num_semanas = 4

# Matriz 3D: [Ciudad][Día][Semana] -> Temperatura
temperaturas = [
    [
        [random.randint(10, 30) for _ in range(num_semanas)]
        for _ in dias_semana
    ]
    for _ in ciudades
]

# 2. Calcular promedios por ciudad y semana
print("Promedios de temperatura:")
for ciudad_idx, ciudad in enumerate(ciudades):
    for semana in range(num_semanas):
        total = 0
        for dia in range(len(dias_semana)):
            total += temperaturas[ciudad_idx][dia][semana]
        promedio = total / len(dias_semana)
        print(f"- {ciudad}: Semana {semana + 1} = {promedio:.1f}°C")
    print()