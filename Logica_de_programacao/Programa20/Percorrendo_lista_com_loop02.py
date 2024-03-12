'''
Programador: Alex Machado Ribeiro
Programa: Percorrendo lista com loop 02
Objetivo: exibir uma lista de nomes.
'''

# declaração de variáveis
lista_nomes = ['Fualno', 'Cicrano', 'Beltrano', 'Joana', 'Maria']

# imprime um item da lista usando laço de repetição
# NOTE: posso usar a função range() para usar um contador para percorrer a lista
for i in range(5):
    print(f'{i + 1}º nome: {lista_nomes[i]}')