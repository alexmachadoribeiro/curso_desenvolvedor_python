'''
Programador: Alex Machado Ribeiro
Programa: Operadores Booleanos
Objetivo: criar um programa que recebe do usuário o nome, idade e altura, e verifica se o usuário tem idade e altura para entrar em um brinquedo de um parque de diversões.
'''

# entrada de dados
nome = input('Informe o nome do usuário: ')
idade = int(input('Informe a idade do usuário: '))
altura = float(input('Informe a altura do usuário em metros: '))

# verifica a idade e altura do usuário ao mesmo tempo
if idade >= 12 and altura >= 1.20:
    print(f'{nome} tem permissão para usar o brinquedo.')
else:
    print(f'{nome} não tem permissão para entrar no brinquedo.')

# NOTE: oepradores booleanos em Python são:
# 'and' para dois valores verdadeiros
# 'or' para pelo menos um valor verdadeiro
# 'not' para um valor falso