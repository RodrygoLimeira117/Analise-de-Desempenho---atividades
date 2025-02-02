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

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

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
    
    merge_sort(numbers)
    
    write_numbers(output_file, numbers)
    elapsed_time = (time.time() - start_time) * 1000  
    final_memory = psutil.Process(os.getpid()).memory_info().rss / 1024
    
    print(f"Tempo de execução (merge_sort): {elapsed_time:.2f} ms")
    print(f"Memória utilizada (merge_sort): {final_memory - initial_memory:.2f} KB")

if __name__ == "__main__":
    main()
