'''
Programador: Alex Machado Ribeiro
Programa: Deleta item em uma posição da lista
Objetivo: usuário deleta um nome em uma posição da lista.
'''

# lista de nomes (array)
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# exibir lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# usuário informa a posição do nome a ser excluído
posicao = int(input('Informe a posição em que está o nome que deseja retirar: '))

# corrigindo a posição
posicao -= 1

# verifica se a posição é válida
if posicao >= 0 and posicao <= 4:
    del(lista_nomes[posicao])
else:
    print('Posição inválida.')

# exibir nova lista
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')