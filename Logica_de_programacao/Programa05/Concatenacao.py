'''
Programador: Alex Machado Ribeiro
Programa: Concatenação
Objetivo: concatenar valores na saída de dados.
'''

# declaração de variáveis
nome = 'Alex Machado Ribeiro'
idade = 39
profissao = 'Programador'

# saída de dados:
# modo 1: estilo Java/JavaScript
# NOTE: essa forma não imrpime números int ou float. É necessário converter para string usando a função 'str'.
print('Olá, meu nome é ' + nome + ', tenho ' + str(idade) + ' anos, e sou ' + profissao + '.')

# modo 2: estilo C/Portugol
# NOTE: nessa forma, os espaços são colocados automaticamente
print('Olá, meu nome é', nome, ', tenho', idade, 'anos, e sou', profissao, '.')

# modo 3: f-string
# NOTE: essa é a melhor forma de exibir os dados, além de permitir quebra de linha com Enter, sem a necessidade de '\n'
print(f'Olá, meu nome é {nome}, tenho {idade} anos, e sou {profissao}.')