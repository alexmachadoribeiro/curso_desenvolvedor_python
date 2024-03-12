'''
Programador: Alex Machado Ribeiro
Programa: Adicionando item no final da lista
Objetivo: usuário insere mais um nome ao final da lista.
'''

# lista de nomes (array)
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# exibir lista original
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')

# usuário informa o nome a ser adicionado
novo_nome = input('Informe um novo nome a ser adicionado ao final da lista: ')

# novo nome é inserido ao final da lista
lista_nomes.append(novo_nome)

# exibir nova lista
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome da lista: {lista_nomes[i]}.')