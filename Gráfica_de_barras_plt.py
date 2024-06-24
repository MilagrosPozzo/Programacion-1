# Inicializar una lista para almacenar los datos de los estudiantes
estudiantes = [
    {"nombre": "Arriola, María", "calificaciones": [10, 8, 6, 10, 9]},
    {"nombre": "Buffa, Lucas", "calificaciones": [10, 9, 8, 6, 9]},
    {"nombre": "Carro, Agustín", "calificaciones": [3, 5, 6, 4, 7]},
    {"nombre": "Noy, Antonhy", "calificaciones": [6, 6, 7, 8, 9]}
]

# Gráfico de barras
import matplotlib.pyplot as plt

from collections import Counter

def grafico_barras_notas(notas):
    contador = Counter(notas)
    notas_unicas = list(contador.keys())
    frecuencias = list(contador.values())
   
   # Configurar las características de la gráfica
    plt.bar(notas_unicas, frecuencias)
    plt.xlabel('Notas')
    plt.ylabel('Frecuencia')
    # Configurar el título de la gráfica
    plt.title('Distribución de Notas')
    plt.xticks(notas_unicas)
    plt.show() # muestra la gráfica luego de que ya se definieron todos los elementos

# Ejemplo de uso:
notas = [7, 8, 6, 9, 7, 8, 10, 6, 8, 7]
grafico_barras_notas(notas)