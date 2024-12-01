const fs = require('fs');
const os = require('os');
const { performance } = require('perf_hooks');

function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
}

function main() {
    const inputFile = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq.txt";
    const outputFile = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq-saida.txt";

    // Leitura do arquivo com o BOM ignorado
    const fileContent = fs.readFileSync(inputFile, 'utf8');  // Lê o arquivo como UTF-8
    const numbers = fileContent.split('\n').filter(Boolean).map(Number); // Filtra linhas vazias e converte para números

    // Informações sobre a linguagem e o sistema
    console.log("Linguagem: JavaScript");
    console.log("Versão: " + process.version);
    console.log("Sistema Operacional: " + os.type());
    console.log("Versão do SO: " + os.release());
    console.log("Processador: " + os.cpus()[0].model);
    console.log("Núcleos de CPU: " + os.cpus().length);

    // Uso de memória antes da execução
    const memBefore = process.memoryUsage().heapUsed / 1024; // Em KB
    console.log(`Memória inicial usada: ${memBefore.toFixed(2)} KB`);

    // Ordenação e medição de tempo
    const startTime = performance.now();
    bubbleSort(numbers);
    const elapsedTime = performance.now() - startTime; // Tempo em ms

    // Uso de memória após execução
    const memAfter = process.memoryUsage().heapUsed / 1024; // Em KB

    // Escrita do arquivo de saída no formato correto (um número por linha)
    fs.writeFileSync(outputFile, numbers.map(num => num + '\n').join(''));

    // Exibição dos resultados
    console.log(`Tempo de execução: ${elapsedTime.toFixed(2)} ms`);
    console.log(`Memória usada após execução: ${(memAfter - memBefore).toFixed(2)} KB`);
    console.log(`Arquivo de saída: ${outputFile}`);
}

main();
