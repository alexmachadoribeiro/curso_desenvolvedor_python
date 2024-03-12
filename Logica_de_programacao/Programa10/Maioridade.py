'''
Programador: Alex Machado Ribeiro
Programa: Maioridade
Objetivo: verificar se o usuário é maior de idade.
'''

# entrada de dados
nome = input('Informe o seu nome: ')
idade = int(input('Informe sua idade: '))

# verifica a idade do usuário
if idade >= 18:
    print(f'{nome} é maior de idade.')
else:
    print(f'{nome} é menor de idade.')