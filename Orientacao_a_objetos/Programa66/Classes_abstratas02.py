'''
Programador: Alex Machado Ribeiro
Programa: Classes Abstratas
Objetivo: trabalhar com classes abstratas.
'''

# faz todos os imports necessários.
import random
from Modulo import *

# entrada de dados.
nome = input('Informe o nome: ')
cpf = input('Informe o CPF: ')

# gera número da conta.
conta = random.randint(100000, 1000000)

# instancia objeto da classe Conta Corrente.
# FIXME: a instancia do objeto irá retornar um erro, pois a classe ainda não possui os métodos da classe abstrata.
conta = ContaCorrente(nome, cpf, conta)

# exibe os atributos da classe.
# NOTE: não será executado, pois o objeto não foi instanciado corretamente.
print(f'Nome: {conta.nome}.')
print(f'CPF: {conta.cpf}.')
print(f'Agência: {conta.agencia}.')
print(f'Conta: {conta.conta}.')
print(f'Saldo: R$ {conta.saldo:,.2f}.')