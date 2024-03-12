'''
Programador: Alex Machado Ribeiro
Programa: Ternário
Objetivo: repetir o programa anterior, usando operador ternário.
'''

# entrada de dados
nome = input('Informe o seu nome: ')
idade = input('Informe sua idade: ')

# a variável precisa ser convertida para inteiro para a verificação
idade = int(idade)

# operador ternário
print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')

# NOTE: use operador ternário quando as alternativas forem pequenas, e quando tiver apenas 2 ou no máximo 3 alternativas