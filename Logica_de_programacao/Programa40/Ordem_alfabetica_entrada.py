'''
Programador: Alex Machado Ribeiro
Programa: Ordem alfabética - entrada
Objetivo: Ordenar nomes informados pelo usuário em ordem alfabética.
'''

# declaração da lista
nomes = []

# usuário insere vários nomes
while True:
    nome = input('Insira um nome, ou deixe o campo vazio e aperte "Enter" para encerrar: ')

    if nome != '':
        nomes.append(nome)
        continue
    else:
        break

# ordena a lista em ordem alfabética
nomes.sort()

# exibe os nomes em ordem alfabética
print(nomes)