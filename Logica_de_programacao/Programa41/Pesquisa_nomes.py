'''
Programador: Alex Machado Ribeiro
Programa: Pesquisa nomes
Objetivo: pesquisar por nomes em uma lista.
'''

# declaração de lista
nomes = ['Fulano','Cicrano','Beltrano','João','Maria','José','Joana','Maria','João','José','Alex','José']

# exibe nomes da lista na tela
for nome in nomes:
    print(nome)

# usuário informa o nome a ser pesquisado
pesquisa_nome = input('Informe o nome que deseja pesquisar: ')

# faz a pesquisa
resultado = pesquisa_nome in nomes

# verifica o resultado
if resultado == True:
    # NOTE: a função 'count()' retorna o número de resultados da busca
    print(f'A pesquisa retornou {nomes.count(pesquisa_nome)} resultados.')
else:
    print('A pesquisa não encontrou nenhum resultado.')