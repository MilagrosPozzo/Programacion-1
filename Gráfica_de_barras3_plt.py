# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt

# Datos predeterminados de los estudiantes
estudiantes = [
    {"nombre": "Arriola, María", "calificaciones": [10, 8, 6, 10, 9]},
    {"nombre": "Buffa, Lucas", "calificaciones": [10, 9, 8, 6, 9]},
    {"nombre": "Carro, Agustín", "calificaciones": [3, 5, 6, 4, 7]},
    {"nombre": "Noy, Antonhy", "calificaciones": [6, 6, 7, 8, 9]}
]

def control_promedio_notas_estudiantes(estudiantes):
    # Inicializamos listas vacías para almacenar los nombres y promedios
    nombres = []
    promedios = []

    # Iteramos sobre cada estudiante en la lista
    for estudiante in estudiantes:
        # Agregamos el nombre del estudiante a la lista de nombres
        nombres.append(estudiante['nombre'])
        
        # Calculamos el promedio de calificaciones del estudiante
        # sum() suma todas las calificaciones y len() cuenta cuántas hay
        promedio = sum(estudiante['calificaciones']) / len(estudiante['calificaciones'])
        
        # Agregamos el promedio calculado a la lista de promedios
        promedios.append(promedio)

    # Creamos una nueva figura con un tamaño específico
    plt.figure(figsize=(6, 6))

    # Creamos el gráfico de barras
    # nombres en el eje x, promedios en el eje y
    plt.bar(nombres, promedios)

    # Personalizamos el gráfico
    plt.title('Control de Promedio de Notas de los Estudiantes')  # Título del gráfico
    plt.xlabel('Estudiantes')  # Etiqueta del eje x
    plt.ylabel('Promedio de Calificaciones')  # Etiqueta del eje y
    plt.ylim(0, 10)  # Establecemos el límite del eje y de 0 a 10

    # Añadimos los valores de los promedios sobre cada barra
    for i, v in enumerate(promedios):
        plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

    # Ajustamos automáticamente el diseño para que todo quede bien
    plt.tight_layout()

    # Mostramos el gráfico
    plt.show()

# Llamamos a la función con nuestros datos de estudiantes
control_promedio_notas_estudiantes(estudiantes)