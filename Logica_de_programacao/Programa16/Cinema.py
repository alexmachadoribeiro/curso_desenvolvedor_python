'''
Programador: Alex Machado Ribeiro
Programa: Cinema
Objetivo: usuário informa o nome e a idade, e escolhe a sala de acordo com o filme que está passando. O programa irá verificar se o usuário tem idade para ver o filme ou não.
Caso não tenha a idade mínima, o programa impede a entrada do usuário e pede para escolher outro filme. Caso o usuário tenha a idade mínima para ver o filme, o programa libera a entrada.
'''

# importa biblioteca
import os

# entrada de dados
nome = input('Informe o seu nome: ')
idade = int(input('Informe a sua idade: '))

# limpaa tela
os.system('cls')

# entra no loop
# NOTE: while True é o equivalente ao 'do...while' das outras linguagens de programação
while True:
    # exibe a lista de filmes
    print('-----CINE COBRA-----\n') # \n executa uma quebra de linha adicional
    print('---Lista de filmes---')
    print('Sala 1 - A Volta dos Que Não Foram - 16 anos.')
    print('Sala 2 - A Roda Quadrada - 14 anos.')
    print('Sala 3 - Poeira em Alto Mar - 12 anos.')
    print('Sala 4 - As Tranças do Rei Careca - Livre.')
    print('Sala 5 - A Vingança do Peixe Frito - 18 anos.\n')

    # usuário informa a sala desejada
    sala = input('Informe a sala desejada: ')

    # limpaa tela
    os.system('cls')

    # NOTE: até recentemente, o Python não possuia uma versão do 'switch...case'. Embora já exista uma versão dela implementada nas versões mais recentes do Python, é recomendado trocar pelo tradicional if...else.
    # verifica a sala
    if sala == '1':
        idade_minima = 16
    elif sala == '2':
        idade_minima = 14
    elif sala == '3':
        idade_minima = 12
    elif sala == '4':
        idade_minima = 0
    elif sala == '5':
        idade_minima = 18
    else:
        print('Sala inexistente. Favor escolher outra sala.')
        continue # interrompe o loop e volta para a próxima execução

    # verifica a idade do usuário
    if idade >= int(idade_minima):
        print(f'{nome} teve a entrada autorizada. Bom filme!')
        break # interrompe e encerra o loop, indo para o final do programa
    else:
        print(f'{nome} não possui a idade mínima para o filme. Favor escolher outro filme.')
        continue
