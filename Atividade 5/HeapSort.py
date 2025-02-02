import platform
import psutil
import time
import os

def read_numbers(file_name):
    numbers = []
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        for line in file:
            try:
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Linha ignorada (não numérica): {line.strip()}")
    return numbers

def write_numbers(file_name, numbers):
    with open(file_name, 'w') as file:
        file.writelines(f"{num}\n" for num in numbers)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def main():
    input_file = r"C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq100k.txt"
    output_file = r"C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq-saida.txt"
    
    print(f"Linguagem: Python")
    print(f"Versão: {platform.python_version()}")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")
    
    initial_memory = psutil.Process(os.getpid()).memory_info().rss / 1024
    
    start_time = time.time()
    numbers = read_numbers(input_file)
    if not numbers:
        print("Nenhum número válido encontrado no arquivo.")
        return
    
    heap_sort(numbers)
    
    write_numbers(output_file, numbers)
    elapsed_time = (time.time() - start_time) * 1000  
    final_memory = psutil.Process(os.getpid()).memory_info().rss / 1024
    
    print(f"Tempo de execução (heap_sort): {elapsed_time:.2f} ms")
    print(f"Memória utilizada (heap_sort): {final_memory - initial_memory:.2f} KB")

if __name__ == "__main__":
    main()
