#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
#Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
#Imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1 
    soma = soma + k
    print(soma)
    
print(soma)

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
#escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibonacci():
    a = 0
    b = 1
    lista_fibonacci = [a, b]

    while True:
        proximo_numero = a + b
        lista_fibonacci.append(proximo_numero)
        a = b
        b = proximo_numero
        if proximo_numero > 1000000:  
            break
    
    return lista_fibonacci

x = int(input("Digite um numero: "))

if x in fibonacci():
    print("Esse numero faz parte da sequência de Fibonacci")
else:
    print("Esse numero não faz parte da sequencia de Fibonacci")

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def carregar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados['faturamento_mensal']

def analisar_faturamento(faturamento):
    faturamento_validos = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

    menor_faturamento = min(faturamento_validos)
    maior_faturamento = max(faturamento_validos)
    media_faturamento = sum(faturamento_validos) / len(faturamento_validos)
    dias_acima_da_media = len([dia for dia in faturamento_validos if dia > media_faturamento])
    
    return menor_faturamento, maior_faturamento, media_faturamento, dias_acima_da_media

arquivo_json = 'faturamento.json'
faturamento_mensal = carregar_faturamento(arquivo_json)

menor, maior, media, dias_acima_media = analisar_faturamento(faturamento_mensal)

print(f"Menor faturamento do mês: {menor:.2f}")
print(f"Maior faturamento do mês: {maior:.2f}")
print(f"Média de faturamento: {media:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total_faturamento = sum(faturamento.values())
percentuais = {estado: (valor / total_faturamento) * 100 for estado, valor in faturamento.items()}
print("Percentual de representação por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

#5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite uma palavra: ")
string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]

print("String invertida:", string_invertida)