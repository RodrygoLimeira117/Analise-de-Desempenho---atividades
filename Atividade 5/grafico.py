import matplotlib.pyplot as plt
import numpy as np

# Dados fornecidos
algoritmos = ["Quick Sort", "Heap Sort", "Merge Sort"]
entradas = ["10k", "50k", "100k"]

tempos_quick = [[49.95, 17.98], [161.45, 85.51], [167.47, 171.90]]
tempos_heap = [[64.99, 68.96], [421.57, 428.78], [868.94, 726.09]]
tempos_merge = [[54.68, 53.95], [318.76, 317.66], [648.09, 610.43]]

# Calculando médias
medias_quick = [np.mean(t) for t in tempos_quick]
medias_heap = [np.mean(t) for t in tempos_heap]
medias_merge = [np.mean(t) for t in tempos_merge]

# Criando gráficos individuais para cada entrada
for i, entrada in enumerate(entradas):
    plt.figure(figsize=(6, 4))
    plt.bar(algoritmos, [medias_quick[i], medias_heap[i], medias_merge[i]], color=['blue', 'orange', 'green'])
    plt.ylabel("Tempo (ms)")
    plt.xlabel("Algoritmo")
    plt.title(f"Tempo de Execução para Entrada {entrada}")
    plt.show()

# Gráfico geral combinando todas as entradas
x_labels = [f"{alg}\n{ent}" for alg in algoritmos for ent in entradas]
y_values = medias_quick + medias_heap + medias_merge
x_positions = np.arange(len(x_labels))

plt.figure(figsize=(10, 5))
plt.bar(x_positions, y_values, color=['blue']*3 + ['orange']*3 + ['green']*3)
plt.ylabel("Tempo (ms)")
plt.xlabel("Algoritmo e Entrada")
plt.xticks(x_positions, x_labels, rotation=45, ha="right")
plt.title("Comparação Geral do Tempo de Execução")
plt.show()

# Exibir as médias
medias_quick, medias_heap, medias_merge
