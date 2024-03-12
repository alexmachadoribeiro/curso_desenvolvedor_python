'''
Programador: Alex Machado Ribeiro
Programa: Separa item da lista
Objetivo: usuário deleta o último nome de uma lista e armazena em uma variável.
'''

# lista de nomes (array)
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# exibir lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# retira o nome da lista e armazena em uma variável
nome_separado = lista_nomes.pop(0)

# exibir nova lista
print('\n-----Nova lista-----\n')
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# exibe o valor que foi sperado da lista
print(f'\nNome serparado: {nome_separado}.\n')