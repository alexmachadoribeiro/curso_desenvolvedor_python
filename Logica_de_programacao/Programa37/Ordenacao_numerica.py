'''
Programador: Alex Machado Ribeiro
Programa: Ordenação numérica
Objetivo: Ordenar números.
'''

# declaração de lista numérica
numeros = [10,1,9,2,8,3,7,4,6,5]

# imprime a lista com os valores atuais
print('Lista com os valores atuais:', numeros)

# ordena a lista atual em ordem cresccente
numeros.sort()

# exibe a lista ordenada
print('Lista ordenada:', numeros)

# ordena a lista em ordem decresccente
numeros.sort(reverse=True)

# exibe a lista reordenada para ordem decrescente
print('Lista em ordem decrescente:', numeros)

# NOTE: existe outra função, a sorted(), que cria uma cópia da lista original e faz a ordenação nela, mantendo a lista original intacta