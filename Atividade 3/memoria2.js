const fs = require("fs");
const os = require("os");

// Função para ler números do arquivo
function readNumbers(fileName) {
    try {
        const content = fs.readFileSync(fileName, "utf-8"); // Lê o arquivo como texto
        const lines = content.split(/\r?\n/); // Divide por linhas
        const numbers = [];
        lines.forEach((line) => {
            const trimmedLine = line.trim(); // Remove espaços extras
            if (!isNaN(trimmedLine) && trimmedLine !== "") {
                numbers.push(parseInt(trimmedLine, 10)); // Converte para inteiro
            } else if (trimmedLine !== "") {
                console.log(`Linha ignorada (não numérica): ${trimmedLine}`);
            }
        });
        return numbers;
    } catch (err) {
        console.error(`Erro ao ler o arquivo: ${err.message}`);
        process.exit(1); // Encerra com erro
    }
}

// Função para escrever números no arquivo
function writeNumbers(fileName, numbers) {
    try {
        const content = numbers.join("\n");
        fs.writeFileSync(fileName, content, "utf-8");
    } catch (err) {
        console.error(`Erro ao escrever o arquivo: ${err.message}`);
        process.exit(1); // Encerra com erro
    }
}

// Função principal
function main() {
    const inputFile = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq.txt";
    const outputFile = "C:\\Users\\rodri\\OneDrive\\Área de Trabalho\\arq-saida.txt";

    console.log("Linguagem: JavaScript");
    console.log(`Versão: ${process.version}`);
    console.log(`Sistema Operacional: ${os.type()} ${os.release()}`);
    console.log(`Processador: ${os.cpus()[0].model}`);

    const initialMemory = process.memoryUsage().rss / 1024; // Em KB
    const startTime = Date.now(); // Início do tempo

    // Lê os números do arquivo e ordena
    const numbers = readNumbers(inputFile);
    if (numbers.length === 0) {
        console.log("Nenhum número válido encontrado no arquivo.");
        return;
    }
    const sortedNumbers = numbers.sort((a, b) => a - b); // Ordena os números
    writeNumbers(outputFile, sortedNumbers); // Grava a saída no arquivo

    const elapsedTime = Date.now() - startTime; // Tempo em ms
    const finalMemory = process.memoryUsage().rss / 1024; // Em KB

    console.log(`Tempo de execução: ${elapsedTime} ms`);
    console.log(`Memória utilizada: ${(finalMemory - initialMemory).toFixed(2)} KB`);
}

main();
