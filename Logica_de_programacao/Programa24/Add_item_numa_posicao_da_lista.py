'''
Programador: Alex Machado Ribeiro
Programa: Adicionando um item em uma posição da lista
Objetivo: usuário insere mais um nome em uma posição selecionada da lista.
'''

# lista de nomes (array)
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# exibir lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# usuário informa o nome a ser adicionado
novo_nome = input('Informe um novo nome a ser adicionado na lista: ')

# usuário informa a posição
posicao = int(input('Informe a posição desejada para adicionar o novo nome: '))

# corrigindo a posição
posicao -= 1

# verifica se a posição é válida
if posicao >= 0 and posicao <= 5:
    lista_nomes.insert(posicao, novo_nome)
else:
    print('Posição inválida.')

# exibir nova lista
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')