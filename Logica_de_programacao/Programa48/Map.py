'''
Programador: Alex Machado Ribeiro
Programa: Map
Objetivo: transformar uma lista numérica em progressão geométrica.
'''

# ANCHOR: lambda
calcular_pg = lambda x: x * 2

# ANCHOR: programa principal
# lista de números
numeros = [1,2,3,4,5]

# aplica a função na lista
# NOTE: A função map permite aplicar uma função a cada elemento de um iterável, como uma lista ou tupla, retornando um novo iterador com os resultados. A função list() retorna uma lista como resultado.
pg = list(map(calcular_pg, numeros))

# exibe a lista original e a lista com pg aplicada
print(f'Lista original: {numeros}.')
print(f'Progressão geométrica: {pg}.')