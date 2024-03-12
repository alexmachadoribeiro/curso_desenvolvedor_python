'''
Programador: Alex Machado Ribeiro
Programa: Loop
Objetivo: usuário irá informar um número inteiro, e o programa irá exibir uma contagem em ordem decrescente.
'''

# entrada de dados
numero = int(input('Informe um número inteiro: '))

# execução do loop
while numero >= 0:
    print(numero)

    # NOTE: se não houver o decremento por parte do contador, o programa irá entrar em loop infinito, travando o pc.
    numero -= 1 # diminui o valor da variável em uma unidade

# NOTE: no Python, não é aceito o operador ++ para incremento ou -- para decremento. Exemplo: numero++ ou numero -- são inválidos.