import matplotlib.pyplot as plt


def calculate_mean(data):
    return sum(data) / len(data)

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


python_time_new = [70090.74, 86167.63, 85375.97, 82884.47, 79921.60, 94393.01, 72145.93, 95161.76, 88075.41, 84869.97]
python_memory_new = [23840, 23760, 23748, 23772, 23692, 23744, 23828, 23884, 23692, 23844]

javascript_time_new = [5976.29, 5723.75, 5543.24, 5950.74, 6061.11, 6058.88, 5785.21, 5724.95, 5879.47, 5525.09]
javascript_memory_new = [6574.48] * 10  


python_time_mean_new = calculate_mean(python_time_new)
python_memory_mean_new = calculate_mean(python_memory_new)
python_time_median_new = calculate_median(python_time_new)
python_memory_median_new = calculate_median(python_memory_new)

javascript_time_mean_new = calculate_mean(javascript_time_new)
javascript_memory_mean_new = calculate_mean(javascript_memory_new)
javascript_time_median_new = calculate_median(javascript_time_new)
javascript_memory_median_new = calculate_median(javascript_memory_new)


languages = ['Python', 'JavaScript']
fig, axs = plt.subplots(4, 2, figsize=(14, 16))
fig.suptitle("Desempenho Atualizado dos Códigos em Python e JavaScript", fontsize=16)


axs[0, 0].plot(python_time_new, marker='o', label='Tempo (ms)', color='blue')
axs[0, 0].axhline(y=python_time_mean_new, color='green', linestyle='--', label=f'Média: {python_time_mean_new:.2f} ms')
axs[0, 0].axhline(y=python_time_median_new, color='red', linestyle='--', label=f'Mediana: {python_time_median_new:.2f} ms')
axs[0, 0].set_title("Python - Tempo")
axs[0, 0].set_xlabel("Execução")
axs[0, 0].set_ylabel("Tempo (ms)")
axs[0, 0].legend()


axs[1, 0].plot(python_memory_new, marker='o', label='Memória (KB)', color='blue')
axs[1, 0].axhline(y=python_memory_mean_new, color='green', linestyle='--', label=f'Média: {python_memory_mean_new:.2f} KB')
axs[1, 0].axhline(y=python_memory_median_new, color='red', linestyle='--', label=f'Mediana: {python_memory_median_new:.2f} KB')
axs[1, 0].set_title("Python - Memória")
axs[1, 0].set_xlabel("Execução")
axs[1, 0].set_ylabel("Memória (KB)")
axs[1, 0].legend()


axs[0, 1].plot(javascript_time_new, marker='o', label='Tempo (ms)', color='orange')
axs[0, 1].axhline(y=javascript_time_mean_new, color='green', linestyle='--', label=f'Média: {javascript_time_mean_new:.2f} ms')
axs[0, 1].axhline(y=javascript_time_median_new, color='red', linestyle='--', label=f'Mediana: {javascript_time_median_new:.2f} ms')
axs[0, 1].set_title("JavaScript - Tempo")
axs[0, 1].set_xlabel("Execução")
axs[0, 1].set_ylabel("Tempo (ms)")
axs[0, 1].legend()


axs[1, 1].plot(javascript_memory_new, marker='o', label='Memória (KB)', color='orange')
axs[1, 1].axhline(y=javascript_memory_mean_new, color='green', linestyle='--', label=f'Média: {javascript_memory_mean_new:.2f} KB')
axs[1, 1].axhline(y=javascript_memory_median_new, color='red', linestyle='--', label=f'Mediana: {javascript_memory_median_new:.2f} KB')
axs[1, 1].set_title("JavaScript - Memória")
axs[1, 1].set_xlabel("Execução")
axs[1, 1].set_ylabel("Memória (KB)")
axs[1, 1].legend()


time_means_new = [python_time_mean_new, javascript_time_mean_new]
memory_means_new = [python_memory_mean_new, javascript_memory_mean_new]

axs[2, 0].bar(languages, time_means_new, color=['blue', 'orange'])
axs[2, 0].set_title("Comparação de Médias - Tempo")
axs[2, 0].set_ylabel("Tempo (ms)")

axs[2, 1].bar(languages, memory_means_new, color=['blue', 'orange'])
axs[2, 1].set_title("Comparação de Médias - Memória")
axs[2, 1].set_ylabel("Memória (KB)")


time_medians_new = [python_time_median_new, javascript_time_median_new]
memory_medians_new = [python_memory_median_new, javascript_memory_median_new]

axs[3, 0].bar(languages, time_medians_new, color=['blue', 'orange'])
axs[3, 0].set_title("Comparação de Medianas - Tempo")
axs[3, 0].set_ylabel("Tempo (ms)")

axs[3, 1].bar(languages, memory_medians_new, color=['blue', 'orange'])
axs[3, 1].set_title("Comparação de Medianas - Memória")
axs[3, 1].set_ylabel("Memória (KB)")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
