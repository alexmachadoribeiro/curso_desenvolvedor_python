'''
Programador: Alex Machado Ribeiro
Programa: Percorrendo lista com loop 03
Objetivo: exibir uma lista de nomes.
'''

# declaração de variáveis
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# imprime um item da lista usando laço de repetição
# NOTE: a função len() retorna o número de itens da lista
for i in range(len(lista_nomes)):
    print(f'{i + 1}º nome: {lista_nomes[i]}')