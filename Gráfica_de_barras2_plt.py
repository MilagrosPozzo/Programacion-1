# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt

# Datos predeterminados
estudiantes = [
    {"nombre": "Arriola, María", "calificaciones": [10, 8, 6, 10, 9]},
    {"nombre": "Buffa, Lucas", "calificaciones": [10, 9, 8, 6, 9]},
    {"nombre": "Carro, Agustín", "calificaciones": [3, 5, 6, 4, 7]},
    {"nombre": "Noy, Antonhy", "calificaciones": [6, 6, 7, 8, 9]}
]

def grafico_barras_estudiantes(estudiantes):
    # Preparar los datos para el gráfico
    nombres = [estudiante['nombre'] for estudiante in estudiantes]
    calificaciones = [estudiante['calificaciones'] for estudiante in estudiantes]

    # Configurar el gráfico
    fig, ax = plt.subplots(figsize=(12, 6))

    # Definir el ancho de las barras y las posiciones
    ancho_barra = 0.15
    r1 = list(range(len(nombres)))
    r2 = [x + ancho_barra for x in r1]
    r3 = [x + ancho_barra for x in r2]
    r4 = [x + ancho_barra for x in r3]
    r5 = [x + ancho_barra for x in r4]

    # Crear las barras para cada calificación
    plt.bar(r1, [c[0] for c in calificaciones], color='#FFA07A', width=ancho_barra, label='Calif 1')
    plt.bar(r2, [c[1] for c in calificaciones], color='#98FB98', width=ancho_barra, label='Calif 2')
    plt.bar(r3, [c[2] for c in calificaciones], color='#87CEFA', width=ancho_barra, label='Calif 3')
    plt.bar(r4, [c[3] for c in calificaciones], color='#DDA0DD', width=ancho_barra, label='Calif 4')
    plt.bar(r5, [c[4] for c in calificaciones], color='#F0E68C', width=ancho_barra, label='Calif 5')

    # Personalizar el gráfico
    plt.xlabel('Estudiantes')
    plt.ylabel('Calificaciones')
    plt.title('Calificaciones por Estudiante')
    plt.xticks([r + ancho_barra*2 for r in range(len(nombres))], nombres, rotation=45, ha='right')

    # Añadir una leyenda
    plt.legend()

    # Ajustar el diseño y mostrar el gráfico
    plt.tight_layout()
    plt.show()

# Llamar a la función para crear el gráfico
grafico_barras_estudiantes(estudiantes)