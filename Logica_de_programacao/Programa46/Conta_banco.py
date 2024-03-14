'''
Programador: Alex Machado Ribeiro
Programa: Banco
Objetivo: criar uma conta em um banco e fazer as operações consultar dados, depositar valor, sacar valor e sair do programa.
'''

# ANCHOR: importa bibliotecas
import os
import random # biblioteca para gerar números aleatórios

# ANCHOR: funções
# função consultar dados
def consultar_dados(nome, cpf, agencia, conta, saldo):
    print(f'Nome do correntista: {nome}.')
    print(f'CPF do correntista: {cpf}.')
    print(f'Agência: {agencia}.')
    print(f'Conta: {conta}.')
    print(f'Saldo atual: R$ {saldo:,.2f}.')

# função mostrar menu
def mostrar_menu():
    print('\n---Menu de opções---\n')
    print('1 - Consultar dados da conta.')
    print('2 - Fazer depósito.')
    print('3 - Fazer saque.')
    print('4 - Sair do programa.')

# ANCHOR: lambdas
# lambda fazer depósito
fazer_deposito = lambda saldo, valor: saldo + valor

# lambda fazer saque
fazer_saque = lambda saldo, valor: saldo - valor

# ANCHOR: programa principal
# início do programa
print('-----BANCO COBRA-----\n')

# criação de conta
nome = input('Informe o nome do correntista: ')
cpf = input('Informe o CPF do correntista: ')
agencia = 10011
conta = random.randint(100000, 1000000) # comando para gerar números aleatórios entre 2 valores
saldo = 0

# limpa tela
os.system('cls')

# mostra dados da nova conta
consultar_dados(nome, cpf, agencia, conta, saldo)

# inicia app
while True:
    # mostra menu de opções
    mostrar_menu()

    # opção escolhida pelo usuário
    opcao = input('Opção desejada: ')

    # limpa tela
    os.system('cls')

    # verifica a opção escolhida pelo usuário
    if opcao == '1':
        print('Consultar dados da conta:')
        consultar_dados(nome, cpf, agencia, conta, saldo)
        continue
    elif opcao == '2':
        print('Fazer depósito:')
        valor = str(input('Informe o valor do depósito: R$ ')).replace(',','.')
        saldo = fazer_deposito(saldo, float(valor))
        print('Depósito efetuado com sucesso.')
        continue
    elif opcao == '3':
        print('Fazer saque:')
        valor = str(input('Informe o valor do saque: R$ ')).replace(',','.')
        valor = float(valor)

        # valor do saque precisa ser menor ou igual ao saldo
        if saldo >= valor:
            saldo = fazer_saque(saldo, valor)
            print('Saque efetuado com sucesso.')
        else:
            print('Não foi possível efetuar o saque.')

        continue
    elif opcao == '4':
        # sai do programa
        print('Obrigado pela preferência.')
        break
    else:
        # invalida a opção escolhida pelo usuário
        print('Opção inválida.')
        continue