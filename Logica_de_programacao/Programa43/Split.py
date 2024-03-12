'''
Programador: Alex Machado Ribeiro
Programa: Split
Objetivo: separar valores em uma lista.
'''

# string com valores unificados
meses_string = 'Janeiro Fevereiro Março'

# separa os valores, nesse caso, o separador é a barra de espaço
meses_lista = meses_string.split(' ')

# exibe a lista na tela
for mes in meses_lista:
    print(mes)

# NOTE: esse algoritmo é útil para separar valores que estão juntos em uma única variável