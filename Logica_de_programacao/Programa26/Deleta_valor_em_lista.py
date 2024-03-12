'''
Programador: Alex Machado Ribeiro
Programa: Deleta valor em lista
Objetivo: usuário deleta um nome baseado em seu valor.
'''

# lista de nomes (array)
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria', 'Beltrano']

# exibir lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# usuário informa o valor que ele deseja retirar da lista
# NOTE: se houver valores repetidos na lista, ele irá remover apenas a primeira ocorrência
nome = input('Informe o nome que deseja retirar da lista: ')

# retira nome da lista
lista_nomes.remove(nome)

# exibir nova lista
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')