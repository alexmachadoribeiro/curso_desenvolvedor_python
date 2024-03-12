'''
Programador: Alex Machado Ribeiro
Programa: Contgem Regressiva
Objetivo: usuário irá informar um número inteiro, e o programa irá exibir uma contagem regressiva.
'''

# importa bibliotecas externas
import os
import time

# entrada de dados
cont = int(input('Insira um número inteiro: '))

# contagem regressiva
while cont >= 0:
    os.system('cls') # limpa a tela do console
    print(f'Contagem regressiva: {cont}...')
    time.sleep(1) # atrasa o próximo comando em 1 segundo
    cont -= 1

# sai do loop e limpa a tela novamente
# NOTE: o comando os.system recebe o comando de acordo com o sistema operacional. No caso, 'cls' é o comando de limpar tela do prompt de comando do Windows
os.system('cls')

# exibe a mensagem final
print('BOOOOMMMM!!!!')