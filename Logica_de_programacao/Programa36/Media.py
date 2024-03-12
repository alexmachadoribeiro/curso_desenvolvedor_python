'''
Programador: Alex Machado Ribeiro
Programa: Média
Objetivo: calcular a média de uma quantidade de números.
'''

# importa biblioteca
import os

# declaração da lista
numeros = []

# usuário insere vários números, na quantidade que desejar
while True:
    numero = str(input('Insira um número, ou deixe o campo vazio e aperte "Enter" para encerrar: ')).replace(',','.')

    # verifica se o valor está vazio ou não
    if numero != '':
        numeros.append(float(numero))
        continue
    else:
        break

# limpa console
os.system('cls')

# exibe os números inseridos
for i in range(len(numeros)):
    print(f'{i + 1}º número: {numeros[i]}')

# calcula a média dos valores inseridos
media = sum(numeros)/len(numeros)

# exibe o resultado
print(f'A média dos números é {media:,.1f}.')