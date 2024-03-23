'''
Programador: Alex Machado Ribeiro
Programa: Encapsulamento
Objetivo: trabalhar com modificadores de acesso no Python.
'''

# ANCHOR: classes

# classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome, idade, cpf):
        self.nome = nome # public
        self._idade = idade # protected
        self.__cpf = cpf # private

    # métodos de acesso
    # NOTE: para acessar os atributos private e protected, precisamos dos métodos set, para enviar os valores, e get, para acessar os valores.
    def set_idade(self, idade):
        self._idade = idade

    def get_idade(self):
        return self._idade

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

    # NOTE: o atributo nome está como public, logo não precisa dos métodos get e set.

# ANCHOR: programa principal
if __name__ == '__main__':
    # instancia o objeto da classe pessoa
    usuario = Pessoa('João', 18, '111.111.111-11')

    # exibe os dados na tela
    # NOTE: o atributo nome não precisa de método get e set, pois é um atributo público.
    print(f'Nome: {usuario.nome}.')

    # NOTE: para acessar os atributos 'idade' e 'cpf', se faz necessário o uso dos métodos 'get'.
    print(f'Idade: {usuario.get_idade()}.')
    print(f'CPF: {usuario.get_cpf()}.')

    # entrada de dados
    novo_nome = input('Insira o novo nome: ')
    nova_idade = int(input('Insira a nova idade: '))
    novo_cpf = input('Insira o novo CPF: ')

    # envia os dados para os atributos
    # NOTE: atributo nome pode ser acessado diretamente.
    usuario.nome = novo_nome

    # NOTE: atributos idade e cpf precisam do método set.
    usuario.set_idade(nova_idade)
    usuario.set_cpf(novo_cpf)

    # exibe os novos dados
    print(f'Novo nome: {usuario.nome}.')
    print(f'Nova idade: {usuario.get_idade()}.')
    print(f'Novo CPF: {usuario.get_cpf()}.')