import matplotlib.pyplot as plt
import numpy as np


python_time = [52.99, 51.99, 52.97, 52.96, 52.99, 58.97, 51.96, 61.95, 62.97, 51.98]
python_memory = [1688, 1676, 1648, 1624, 1612, 1716, 1616, 1668, 1688, 1604]

javascript_time = [33, 32, 30, 30, 39, 29, 32, 30, 29, 30]
javascript_memory = [8160, 8112, 8392, 8448, 8108, 8212, 8092, 8116, 8400, 8112]


def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)


python_time_mean = calculate_mean(python_time)
python_memory_mean = calculate_mean(python_memory)
python_time_median = calculate_median(python_time)
python_memory_median = calculate_median(python_memory)

javascript_time_mean = calculate_mean(javascript_time)
javascript_memory_mean = calculate_mean(javascript_memory)
javascript_time_median = calculate_median(javascript_time)
javascript_memory_median = calculate_median(javascript_memory)


fig, axs = plt.subplots(4, 2, figsize=(14, 16))
fig.suptitle("Desempenho dos Códigos em Python e JavaScript", fontsize=16)


axs[0, 0].plot(python_time, marker='o', label='Tempo (ms)', color='blue')
axs[0, 0].axhline(y=python_time_mean, color='green', linestyle='--', label=f'Média: {python_time_mean:.2f} ms')
axs[0, 0].axhline(y=python_time_median, color='red', linestyle='--', label=f'Mediana: {python_time_median:.2f} ms')
axs[0, 0].set_title("Python - Tempo")
axs[0, 0].set_xlabel("Execução")
axs[0, 0].set_ylabel("Tempo (ms)")
axs[0, 0].legend()


axs[1, 0].plot(python_memory, marker='o', label='Memória (KB)', color='blue')
axs[1, 0].axhline(y=python_memory_mean, color='green', linestyle='--', label=f'Média: {python_memory_mean:.2f} KB')
axs[1, 0].axhline(y=python_memory_median, color='red', linestyle='--', label=f'Mediana: {python_memory_median:.2f} KB')
axs[1, 0].set_title("Python - Memória")
axs[1, 0].set_xlabel("Execução")
axs[1, 0].set_ylabel("Memória (KB)")
axs[1, 0].legend()


axs[0, 1].plot(javascript_time, marker='o', label='Tempo (ms)', color='orange')
axs[0, 1].axhline(y=javascript_time_mean, color='green', linestyle='--', label=f'Média: {javascript_time_mean:.2f} ms')
axs[0, 1].axhline(y=javascript_time_median, color='red', linestyle='--', label=f'Mediana: {javascript_time_median:.2f} ms')
axs[0, 1].set_title("JavaScript - Tempo")
axs[0, 1].set_xlabel("Execução")
axs[0, 1].set_ylabel("Tempo (ms)")
axs[0, 1].legend()


axs[1, 1].plot(javascript_memory, marker='o', label='Memória (KB)', color='orange')
axs[1, 1].axhline(y=javascript_memory_mean, color='green', linestyle='--', label=f'Média: {javascript_memory_mean:.2f} KB')
axs[1, 1].axhline(y=javascript_memory_median, color='red', linestyle='--', label=f'Mediana: {javascript_memory_median:.2f} KB')
axs[1, 1].set_title("JavaScript - Memória")
axs[1, 1].set_xlabel("Execução")
axs[1, 1].set_ylabel("Memória (KB)")
axs[1, 1].legend()


languages = ['Python', 'JavaScript']
time_means = [python_time_mean, javascript_time_mean]
memory_means = [python_memory_mean, javascript_memory_mean]

axs[2, 0].bar(languages, time_means, color=['blue', 'orange'])
axs[2, 0].set_title("Comparação de Médias - Tempo")
axs[2, 0].set_ylabel("Tempo (ms)")

axs[2, 1].bar(languages, memory_means, color=['blue', 'orange'])
axs[2, 1].set_title("Comparação de Médias - Memória")
axs[2, 1].set_ylabel("Memória (KB)")


time_medians = [python_time_median, javascript_time_median]
memory_medians = [python_memory_median, javascript_memory_median]

axs[3, 0].bar(languages, time_medians, color=['blue', 'orange'])
axs[3, 0].set_title("Comparação de Medianas - Tempo")
axs[3, 0].set_ylabel("Tempo (ms)")

axs[3, 1].bar(languages, memory_medians, color=['blue', 'orange'])
axs[3, 1].set_title("Comparação de Medianas - Memória")
axs[3, 1].set_ylabel("Memória (KB)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
