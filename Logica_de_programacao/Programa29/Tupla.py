'''
Programador: Alex Machado Ribeiro
Programa: Tupla
Objetivo: exibir uma tupla.
'''

# tupla
# NOTE: uma tupla é um tipo de lista que não pode ser alterada
cidades = ('Brasília', 'Rio de Janeiro', 'São Paulo', 'Goiânia', 'São Luiz')

# imprime os itens da tupla
for i in range(len(cidades)):
    print(f'{i + 1}: {cidades[i]}')

# FIXME: se tentar alterar algum dado da tupla, o código dá erro
cidades[0] = 'Belo Horizonte'

# NOTE: o erro do 'fixme' foi aplicado propositalmente, para mostrar que tipo de erro dá quando se tenta alterar uma tupla