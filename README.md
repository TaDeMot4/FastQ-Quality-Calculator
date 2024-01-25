Calculadora de FastQ

Este script é usado para calcular a média da pontuação de qualidade e o comprimento da sequência de leituras em um arquivo FASTQ e filtrar as leituras com base nessas métricas.

Uso
python3 Aleff_Aquino_202300054-Diogo_Mota_202300409-fastq_parser in_file.fastq output_file.fastq -value x -len y
onde x é o valor de corte para a pontuação de qualidade média e y é o valor de corte para o comprimento da sequência. Pelo menos uma informação deve ser validada, isto é, pelo menos um -value ou -len deve ser concedido para funcionalidade do script.

Exemplo
Para filtrar leituras com uma pontuação de qualidade média de pelo menos 30 e um comprimento de sequência de pelo menos 100 bases, use o seguinte comando:

python3 Aleff_Aquino_202300054-Diogo_Mota_202300409-fastq_parser in_file.fastq output_file.fastq -value 30 -len 100
Saída
O script gerará um arquivo FASTQ filtrado chamado output_file.fastq. O relatório de filtragem será impresso no console.

Requisitos
Este script requer as seguintes bibliotecas:

- argparse

Você pode instalar essas bibliotecas usando o seguinte comando:

pip install argparse

Explicação

O script funciona da seguinte forma:

Ele lê o arquivo FASTQ de entrada, linha por linha.
Para cada linha, ele calcula a pontuação de qualidade média dos caracteres de qualidade.
Ele armazena as pontuações de qualidade média e os comprimentos das sequências em listas.
Ele filtra as leituras com base nos valores de corte especificados pelo usuário.
Ele escreve as leituras filtradas em um arquivo FASTQ de saída.
Opções de linha de comando

As seguintes opções de linha de comando estão disponíveis:

-value ou --cutoff_value: especifica o valor de corte para a pontuação de qualidade média.
-len ou --cutoff_length: especifica o valor de corte para o comprimento da sequência.
Ao menos um dos parâmetros deve ser especificado, se voce deseja realizar um corte apenas por comprimento utilize apenas -len, caso queira apenas por qualidade utilize -value apenas. O script também correrá caso forneça os dois parâmetros.

Exemplos

Aqui estão alguns exemplos de como usar o script:

Para filtrar todas as leituras com uma pontuação de qualidade média de pelo menos 30, use o seguinte comando:
python3 Aleff_Aquino_202300054-Diogo_Mota_202300409-fastq_parser in_file.fastq output_file.fastq -value 30
Para filtrar todas as leituras com um comprimento de sequência de pelo menos 100 bases, use o seguinte comando:
python3 Aleff_Aquino_202300054-Diogo_Mota_202300409-fastq_parser in_file.fastq output_file.fastq -len 100
Para filtrar todas as leituras com uma pontuação de qualidade média de pelo menos 30 e um comprimento de sequência de pelo menos 100 bases, use o seguinte comando:
python3 Aleff_Aquino_202300054-Diogo_Mota_202300409-fastq_parser in_file.fastq output_file.fastq -value 30 -len 100