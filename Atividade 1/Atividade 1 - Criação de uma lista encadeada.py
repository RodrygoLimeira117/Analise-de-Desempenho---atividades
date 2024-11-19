import time

class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, valor):
        novo_no = No(valor)
        if not self.cabeca:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no

    def inserir(self, valor, posicao):
        novo_no = No(valor)
        if posicao == 0:
            novo_no.proximo = self.cabeca
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            for _ in range(posicao - 1):
                if not atual.proximo:
                    break
                atual = atual.proximo
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no

    def remover(self, valor):
        atual = self.cabeca
        if atual and atual.valor == valor:
            self.cabeca = atual.proximo
            return
        anterior = None
        while atual and atual.valor != valor:
            anterior = atual
            atual = atual.proximo
        if atual:
            anterior.proximo = atual.proximo

    def mostrar(self):
        elementos = []
        atual = self.cabeca
        while atual:
            elementos.append(atual.valor)
            atual = atual.proximo
        print(" -> ".join(map(str, elementos)))

def processar_arquivo(caminho):
    try:
        with open(caminho, 'r', encoding='utf-8-sig') as arquivo:
            linhas = arquivo.readlines()

        valores_iniciais = list(map(int, linhas[0].split()))
        lista = ListaEncadeada()
        for valor in valores_iniciais:
            lista.adicionar(valor)

        for linha in linhas[2:]:
            partes = linha.split()
            if partes[0] == 'A':
                lista.inserir(int(partes[1]), int(partes[2]))
            elif partes[0] == 'R':
                lista.remover(int(partes[1]))
            elif partes[0] == 'P':
                lista.mostrar()



    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Caminhos dos arquivos
if __name__ == "__main__":
    arquivo1 = r"C:\Users\rodri\OneDrive\Área de Trabalho\arq.txt"

    start_time = time.time()  # Captura o tempo inicial
    print("Resultados para arq.txt:")
    processar_arquivo(arquivo1)

    end_time = time.time()  # Captura o tempo final

    print(f"\nTempo total de execução: {end_time - start_time:.4f} segundos")