'''
Programador: Alex Machado Ribeiro
Programa: Classes Abstratas
Objetivo: trabalhar com classes abstratas.
'''

# faz todos os imports necessários.
import random
import os
from Modulo import *

# entrada de dados.
nome = input('Informe o nome: ')
cpf = input('Informe o CPF: ')

# gera número da conta.
conta = random.randint(100000, 1000000)

# instancia objeto da classe Conta Corrente.
conta = ContaCorrente(nome, cpf, conta)

# limpa console
os.system('cls')

# exibe os dados da conta
conta.consultar_dados()

# entrar no loop.
while True:
    # exibe o menu
    print('-----BANCO COBRA-----\n')
    print('1 - Consultar dados da conta.')
    print('2 - Fazer depósito.')
    print('3 - Fazer saque.')
    print('4 - Sair do programa.\n')

    # usuário informa a opção desejada
    opcao = input('Opção desejada: ')

    # limpa console
    os.system('cls')

    # verifica a opção informada pelo cliente.
    if opcao == '1':
        conta.consultar_dados()
        continue
    elif opcao == '2':
        valor = str(input('Informe o valor do depósito: R$ ')).replace(',', '.')
        valor = float(valor)
        conta.saldo = conta.fazer_deposito(valor)
        print('Depósito efetuado com sucesso!')
        continue
    elif opcao == '3':
        valor = str(input('Informe o valor do saque: R$ ')).replace(',', '.')
        valor = float(valor)

        if valor <= conta.saldo:
            conta.saldo = conta.fazer_saque(valor)
            print('Saque efetuado com sucesso!')
        else:
            print('Não foi possível efetuar o saque!')

        continue
    elif opcao == '4':
        print('Programa finalizado com sucesso!')
        break
    else:
        print('Opção inválida!')
        continue

    # NOTE: na prática, utilizamos as classes abstratas em Python com o mesmo objetivo das interfaces em Java ou PHP.