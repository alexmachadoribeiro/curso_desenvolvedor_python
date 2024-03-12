'''
Programador: Alex Machado Ribeiro
Programa: Operadores Aritméticos
Objetivo: usuário irá informar dois números inteiros, e o programa retorna o resultado das 4 operações básicas, mais o resto da divisão.
'''

# entrada de dados
n1 = input('Informe um número inteiro: ')
n2 = input('Informe outro número inteiro: ')

# NOTE: o Python reconhece a entrada de dados como string. Portanto, é necessário converter para int ou float quando necessário

# converte as entradas de dados em inteiros
n1 = int(n1)
n2 = int(n2)

# operações matemáticas
soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
resto = n1 % n2

# saída de dados
print(f'Soma: {soma}')
print(f'Subtração: {subtracao}')
print(f'Multiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')
print(f'Resto da divisão: {resto}')