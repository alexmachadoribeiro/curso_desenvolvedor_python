'''
Programador: Alex Machado Ribeiro
Programa: Função
Objetivo: criar uma função que calcule a equação do 1º grau.
'''

# NOTE: as funções servem para separar o código em blocos menores, facilitando a manutenção do código.

# ANCHOR: função que calcula a equação do 1º grau
# NOTE: os valores dentro do parênteses são os parâmetros da função. O comando 'return' é o valor que a função retorna.
def calcular_primeiro_grau(a, b):
    x = -b/a
    return x # retorno da função

# NOTE: não é obrigatório que a função possua parâmetros, nem que ela retorne algo. Pergunte se a função precisa de um ou mais valores externos a ela, ou se ela precisa enviar algum valor para o algoritmo principal

# ANCHOR: programa principal
# exibe na tela a equação do 1º grau
print('-----CALCULAR A EQUAÇÃO DO 1º GRAU-----\n')
print('Equação do 1º grau: ax+b=0')

# usuário informa os valores da equação
a = int(input('Informe o valor de "a": '))
b = int(input('Informe o valor de "b: '))

# exibe a equação do 1º grau montada
if b >= 0:
    print(f'\n{a}x+{b}=0\n')
else:
    print(f'\n{a}x{b}=0\n')

# calcula a função
resultado = calcular_primeiro_grau(a, b) # os valores informados pelo usuário são repassados para a função, que por sua vez retorna um valor para a variável "resultado"

# imprime o resultado na tela
print(f'O valor de "x" é {resultado}.')