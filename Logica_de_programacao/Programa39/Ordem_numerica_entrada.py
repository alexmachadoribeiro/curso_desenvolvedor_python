'''
Programador: Alex Machado Ribeiro
Programa: Ordem numérica - entrada
Objetivo: Ordenar números informados pelo usuário em ordem crescente.
'''

# declaração da lista
numeros = []

# usuário insere vários números
while True:
    numero = str(input('Insira um número, ou deixe o campo vazio e aperte "Enter" para encerrar: ')).replace(',','.')

    if numero != '':
        numeros.append(float(numero))
        continue
    else:
        break

# ordena os números em ordem numérica
numeros.sort()

# exibe os números ordenados na tela
print(numeros)