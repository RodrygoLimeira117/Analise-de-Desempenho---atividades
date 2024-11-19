class No {
    constructor(valor) {
        this.valor = valor;
        this.proximo = null;
    }
}

class ListaEncadeada {
    constructor() {
        this.cabeca = null;
    }

    adicionar(valor) {
        const novoNo = new No(valor);
        if (!this.cabeca) {
            this.cabeca = novoNo;
        } else {
            let atual = this.cabeca;
            while (atual.proximo) {
                atual = atual.proximo;
            }
            atual.proximo = novoNo;
        }
    }

    inserir(valor, posicao) {
        const novoNo = new No(valor);
        if (posicao === 0) {
            novoNo.proximo = this.cabeca;
            this.cabeca = novoNo;
        } else {
            let atual = this.cabeca;
            for (let i = 0; i < posicao - 1; i++) {
                if (!atual.proximo) break;
                atual = atual.proximo;
            }
            novoNo.proximo = atual.proximo;
            atual.proximo = novoNo;
        }
    }

    remover(valor) {
        let atual = this.cabeca;
        if (atual && atual.valor === valor) {
            this.cabeca = atual.proximo;
            return;
        }
        let anterior = null;
        while (atual && atual.valor !== valor) {
            anterior = atual;
            atual = atual.proximo;
        }
        if (atual) {
            anterior.proximo = atual.proximo;
        }
    }

    mostrar() {
        const elementos = [];
        let atual = this.cabeca;
        while (atual) {
            elementos.push(atual.valor);
            atual = atual.proximo;
        }
        console.log(elementos.join(" -> "));
    }
}

async function processarArquivo(caminho) {
    const fs = require('fs').promises;

    try {
        const conteudo = await fs.readFile(caminho, 'utf-8');
        const linhas = conteudo.split('\n').map(linha => linha.trim()).filter(linha => linha);

        const valoresIniciais = linhas[0].split(' ').map(Number);
        const lista = new ListaEncadeada();

        valoresIniciais.forEach(valor => lista.adicionar(valor));

        for (let i = 2; i < linhas.length; i++) {
            const partes = linhas[i].split(' ');
            if (partes[0] === 'A') {
                lista.inserir(Number(partes[1]), Number(partes[2]));
            } else if (partes[0] === 'R') {
                lista.remover(Number(partes[1]));
            } else if (partes[0] === 'P') {
                lista.mostrar();
            }
        }
    } catch (error) {
        if (error.code === 'ENOENT') {
            console.error(`Erro: Arquivo '${caminho}' não encontrado.`);
        } else {
            console.error(`Ocorreu um erro: ${error.message}`);
        }
    }
}

// Caminho do arquivo
(async () => {
    const caminhoArquivo = 'C:/Users/rodri/OneDrive/Área de Trabalho/arq.txt';

    console.log('Resultados para arq.txt:');
    const startTime = Date.now();

    await processarArquivo(caminhoArquivo);

    const endTime = Date.now();
    console.log(`\nTempo total de execução: ${(endTime - startTime) / 1000} segundos`);
})();
