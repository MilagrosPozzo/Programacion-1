# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
from collections import Counter

# Suponemos que ya tenemos definida la lista 'estudiantes'
# Inicializar una lista para almacenar los datos de los estudiantes
estudiantes = [
    {"nombre": "Arriola, María", "calificaciones": [10, 8, 6, 10, 9]},
    {"nombre": "Buffa, Lucas", "calificaciones": [10, 9, 8, 6, 9]},
    {"nombre": "Carro, Agustín", "calificaciones": [3, 5, 6, 4, 7]},
    {"nombre": "Noy, Antonhy", "calificaciones": [6, 6, 7, 8, 9]}
]

def grafico_barras_notas(estudiantes):
    # Recopilar todas las notas en una lista
    todas_las_notas = [nota for estudiante in estudiantes for nota in estudiante['calificaciones']]
    
    # Contar la frecuencia de cada nota
    contador = Counter(todas_las_notas)
    
    # Preparar los datos para el gráfico
    notas = list(contador.keys())
    frecuencias = list(contador.values())
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(notas, frecuencias)
    
    # Personalizar el gráfico
    plt.title('Distribución de Notas')
    plt.xlabel('Notas')
    plt.ylabel('Frecuencia')
    plt.xticks(range(min(notas), max(notas)+1))
    
    # Mostrar el gráfico
    plt.show()

# Llamar a la función para crear el gráfico
grafico_barras_notas(estudiantes)