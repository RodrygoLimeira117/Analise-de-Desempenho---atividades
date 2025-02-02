import platform
import psutil
import time
import os

# Lê números do arquivo, ignorando linhas inválidas
def read_numbers(file_name):
    numbers = []
    with open(file_name, 'r', encoding='utf-8-sig') as file:  # Remove o BOM automaticamente
        for line in file:
            try:
                # Tenta converter para inteiro, ignorando espaços extras
                number = int(line.strip())
                numbers.append(number)
            except ValueError:
                print(f"Linha ignorada (não numérica): {line.strip()}")
    return numbers

# Escreve os números ordenados no arquivo de saída
def write_numbers(file_name, numbers):
    with open(file_name, 'w') as file:
        file.writelines(f"{num}\n" for num in numbers)

def main():
    input_file = r"C:\Users\rodri\OneDrive\Área de Trabalho\arq100k.txt"
    output_file = r"C:\Users\rodri\OneDrive\Área de Trabalho\arq-saida.txt"


    print(f"Linguagem: Python")
    print(f"Versão: {platform.python_version()}")
    print(f"Sistema Operacional: {platform.system()} {platform.release()}")
    print(f"Processador: {platform.processor()}")


    initial_memory = psutil.Process(os.getpid()).memory_info().rss / 1024  # Em KB


    start_time = time.time()
    numbers = read_numbers(input_file)
    if not numbers:
        print("Nenhum número válido encontrado no arquivo.")
        return
    sorted_numbers = sorted(numbers)
    write_numbers(output_file, sorted_numbers)
    elapsed_time = (time.time() - start_time) * 1000  # Em ms


    final_memory = psutil.Process(os.getpid()).memory_info().rss / 1024  # Em KB

    print(f"Tempo de execução: {elapsed_time:.2f} ms")
    print(f"Memória utilizada: {final_memory - initial_memory:.2f} KB")

if __name__ == "__main__":
    main()
