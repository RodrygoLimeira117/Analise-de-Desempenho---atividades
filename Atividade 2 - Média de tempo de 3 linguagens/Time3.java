import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

class No {
    int valor;
    No proximo;

    public No(int valor) {
        this.valor = valor;
        this.proximo = null;
    }
}

class ListaEncadeada {
    No cabeca;

    public ListaEncadeada() {
        this.cabeca = null;
    }

    public void adicionar(int valor) {
        No novoNo = new No(valor);
        if (cabeca == null) {
            cabeca = novoNo;
        } else {
            No atual = cabeca;
            while (atual.proximo != null) {
                atual = atual.proximo;
            }
            atual.proximo = novoNo;
        }
    }

    public void inserir(int valor, int posicao) {
        No novoNo = new No(valor);
        if (posicao == 0) {
            novoNo.proximo = cabeca;
            cabeca = novoNo;
        } else {
            No atual = cabeca;
            for (int i = 0; i < posicao - 1; i++) {
                if (atual.proximo == null) break;
                atual = atual.proximo;
            }
            novoNo.proximo = atual.proximo;
            atual.proximo = novoNo;
        }
    }

    public void remover(int valor) {
        No atual = cabeca;
        if (atual != null && atual.valor == valor) {
            cabeca = atual.proximo;
            return;
        }
        No anterior = null;
        while (atual != null && atual.valor != valor) {
            anterior = atual;
            atual = atual.proximo;
        }
        if (atual != null) {
            anterior.proximo = atual.proximo;
        }
    }

    public void mostrar() {
        StringBuilder elementos = new StringBuilder();
        No atual = cabeca;
        while (atual != null) {
            elementos.append(atual.valor).append(" -> ");
            atual = atual.proximo;
        }
        if (elementos.length() > 0) {
            elementos.setLength(elementos.length() - 4); // Remove o último " -> "
        }
        System.out.println(elementos);
    }
}

public class Time3 {
    public static void processarArquivo(String caminho) {
        try {
            // Lê todas as linhas do arquivo, removendo o BOM se existir
            List<String> linhas = Files.readAllLines(Paths.get(caminho), StandardCharsets.UTF_8);

            ListaEncadeada lista = new ListaEncadeada();

            // Remover o BOM da primeira linha, se necessário
            if (!linhas.isEmpty()) {
                String primeiraLinha = linhas.get(0).replace("\uFEFF", "");
                String[] valoresIniciais = primeiraLinha.split(" ");
                for (String valor : valoresIniciais) {
                    try {
                        lista.adicionar(Integer.parseInt(valor));
                    } catch (NumberFormatException e) {
                        System.err.println("Valor inválido ignorado na linha inicial: " + valor);
                    }
                }
            }

            // Processar as operações subsequentes
            for (int i = 1; i < linhas.size(); i++) {
                String linha = linhas.get(i).trim();
                if (!linha.isEmpty()) {
                    String[] partes = linha.split(" ");
                    try {
                        if (partes[0].equals("A")) {
                            lista.inserir(Integer.parseInt(partes[1]), Integer.parseInt(partes[2]));
                        } else if (partes[0].equals("R")) {
                            lista.remover(Integer.parseInt(partes[1]));
                        } else if (partes[0].equals("P")) {
                            lista.mostrar();
                        } else {
                            System.err.println("Comando inválido ignorado: " + partes[0]);
                        }
                    } catch (NumberFormatException e) {
                        System.err.println("Erro ao processar operação na linha: " + linha);
                    }
                }
            }
        } catch (IOException e) {
            System.err.println("Erro: Arquivo '" + caminho + "' não encontrado.");
        }
    }

    public static void main(String[] args) {
        String caminhoArquivo = "C:/Users/rodri/Downloads/Analise de Desempenho - atividades/arq.txt";

        System.out.println("Resultados para arq.txt:");

        long startTime = System.currentTimeMillis(); // Tempo de início

        processarArquivo(caminhoArquivo);

        long endTime = System.currentTimeMillis(); // Tempo de término
        System.out.println("\nTempo total de execução: " + (endTime - startTime) / 1000.0 + " segundos");
    }
}
