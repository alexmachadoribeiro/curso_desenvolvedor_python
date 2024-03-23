'''
Programador: Alex Machado Ribeiro
Programa: Herança
Objetivo: trabalhar com heranças de classes no Python.
'''

# faz a importação das classe e de uma biblioteca externa
from Modulo import *
import os

# entrada de dados do usuário
nome = input('Informe o nome do usuário: ')
email = input('Informe o e-mail do usuário: ')
endereco = input('Informe o endereço do usuário: ')
cpf = input('Informe o CPF do usuário: ')
cargo = input('Informe o cargo em que o usuário trabalha: ')

# instancia o objeto do tipo pessoa física
empregado = PessoaFisica(nome, email, endereco, cpf, cargo)

# entrada de dados da empresa
nome = input('Informe o nome da empresa: ')
email = input('Informe o e-mail da empresa: ')
endereco = input('Informe o endereço da empresa: ')
cnpj = input('Informe o CNPJ da empresa: ')
setor = input('Informe o setor de atuação da empresa: ')

# instancia objeto do tipo pessoa jurídica
empresa = PessoaJuridica(nome, email, endereco, cnpj, setor)

# limpa console
os.system('cls')

# saída de dados do objeto pessoa física
print('DADOS DO EMPREGADO:\n')
print(f'Nome do empregado: {empregado.nome}.')
print(f'E-mail do empregado: {empregado.email}.')
print(f'Endereço do empregado: {empregado.endereco}.')
print(f'CPF do empregado: {empregado.cpf}.')
print(f'Cargo do empregado: {empregado.cargo}.')

# saída de dados da pessoa jurídica
print('\nDADOS DA EMPRESA:\n')
print(f'Nome da empresa: {empresa.nome}.')
print(f'E-mail da empresa: {empresa.email}.')
print(f'Endereço da empresa: {empresa.endereco}.')
print(f'CNPJ da empresa: {empresa.cnpj}.')
print(f'Setor de atuação da empresa: {empresa.setor}.\n')