import os
import platform
import psutil
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    input_file = r"C:\Users\rodri\OneDrive\Área de Trabalho\arq.txt"
    output_file = r"C:\Users\rodri\OneDrive\Área de Trabalho\arq-saida.txt"


    with open(input_file, "r", encoding="utf-8-sig") as file:
        numbers = [int(line.strip()) for line in file]


    print(f"Linguagem: Python")
    print(f"Versão: {platform.python_version()}")
    print(f"Sistema Operacional: {platform.system()}")
    print(f"Versão do SO: {platform.release()}")
    print(f"Processador: {platform.processor()}")

    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss / 1024  # Memória em KB
    cpu_cores = psutil.cpu_count(logical=True)

    print(f"Núcleos de CPU disponíveis: {cpu_cores}")
    print(f"Memória inicial usada: {mem_before:.2f} KB")

    start_time = time.time()
    bubble_sort(numbers)
    elapsed_time = (time.time() - start_time) * 1000  # Tempo em ms


    mem_after = process.memory_info().rss / 1024  # Memória em KB

    with open(output_file, "w", encoding="utf-8-sig") as file:
        for number in numbers:
            file.write(f"{number}\n")

    print(f"Tempo de execução: {elapsed_time:.2f} ms")
    print(f"Memória usada após execução: {mem_after - mem_before:.2f} KB")
    print(f"Arquivo de saída: {output_file}")

if __name__ == "__main__":
    main()

