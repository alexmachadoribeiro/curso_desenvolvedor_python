'''
Programador: Alex Machado Ribeiro
Programa: Lambda
Objetivo: criar funções lambda que calculem as operações básicas da matemática.
'''

# NOTE: funções lambda são funções que o usuário não precisa definir, ou seja, não vai precisar escrever a função e depois utilizá-la dentro do código.

# funções lambda
# NOTE: funções lambda são ideais quando se deseja criar funções que possuem apenas o retorno
soma = lambda x, y: x + y
subtracao = lambda x, y: x - y
multiplicacao = lambda x, y: x * y
divisao = lambda x, y: x / y
resto = lambda x, y: x % y
potencia = lambda x, y: x ** y

# função normal para exibir um menu
# NOTE: esse é um exemplo de uma função que não recebe parâmetros nem retorna nada
def exibir_menu():
    print('---ESCOLHA A OPERAÇÃO DESEJADA---\n')
    print('+ para somar.')
    print('- para subtrair.')
    print('* para multiplicar.')
    print('/ para dividir.')
    print('% para calcular o resto da divisão.')
    print('** para calcular a potenciação do primeiro número elevado ao segundo número.\n')

# inicio do loop
while True:
    # entrada de dados
    x = int(input('Informe um número inteiro: '))
    y = int(input('Informe outro número inteiro: '))

    # exibe o menu
    exibir_menu()

    # lê a operação desejada pelo usuário
    operacao = input('Qual a operação desejada? ')

    # verifica a operação escolhida pelo usuário
    while True:
        if operacao == '+':
            print(f'O resultado da soma entre {x} e {y} é {soma(x, y)}.')
            break
        elif operacao == '-':
            print(f'O resultado da subtração {x} e {y} é {subtracao(x, y)}.')
            break
        elif operacao == '*':
            print(f'O resultado da multiplicação {x} e {y} é {multiplicacao(x, y)}.')
            break
        elif operacao == '/':
            print(f'O resultado da divisão {x} e {y} é {divisao(x, y)}.')
            break
        elif operacao == '%':
            print(f'O resto da divisão {x} e {y} é {resto(x, y)}.')
            break
        elif operacao == '**':
            print(f'O resultado da potenciação {x} e {y} é {potencia(x, y)}.')
            break
        else:
            print('Operação não disponível.')
            continue

    # pergunta ao usuário se deseja continuar
    continuar = input('Deseja continuar (s/n)? ')

    # verifica se o usuário deseja continuar ou não
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print('Opção inválida. Programa encerrado.')
        break