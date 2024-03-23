'''
Programador: Alex Machado Ribeiro
Programa: Encapsulamento
Objetivo: trabalhar com modificadores de acesso no Python.
'''

# ANCHOR: classes

# classe pessoa
class Pessoa:
    # construtor
    # NOTE: desta vez, vamos definir todos os atributos como private.
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    # métodos de acesso
    # NOTE: em Python, costuma-se usar @property para métodos get e @atributo.setter para métodos set.
    # método get nome
    @property
    def nome(self):
        return self.__nome

    # método set nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

# ANCHOR: programa principal
if __name__ == '__main__':
    # instancia o objeto pessoa
    usuario = Pessoa('João', 18, '111.111.111-11')

    # NOTE: a vantagem de se usar @property e @atributo.setter é poder acessar os atributos protegidos de forma direta, como se eles fossem public.

    # exibe os atributos na tela
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'CPF: {usuario.cpf}.')

    # entrada de dados
    novo_nome = input('Insira o novo nome: ')
    nova_idade = int(input('Insira a nova idade: '))
    novo_cpf = input('Insira o novo CPF: ')

    # atribui os novos valores
    usuario.nome = novo_nome
    usuario.idade = nova_idade
    usuario.cpf = novo_cpf

    # exibe os novos dados
    print(f'Novo nome: {usuario.nome}.')
    print(f'Nova idade: {usuario.idade}.')
    print(f'Novo CPF: {usuario.cpf}.')