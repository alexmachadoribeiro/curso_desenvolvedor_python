'''
Programador: Alex Machado Ribeiro
Programa: Encapsulamento
Objetivo: trabalhar com modificadores de acesso no Python.
'''

# ANCHOR: classes

# NOTE: os métodos de acesso são public, private e protected.
# No Python, são acessados através dos prefixos _ (1 underscore para protected) e __ (2 underscores para private).
# O objetivo é fornecer uma certa proteção ao acesso aos atributos.

# classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome, idade, cpf):
        self.nome = nome # public
        self._idade = idade # protected
        self.__cpf = cpf # private

# ANCHOR: programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input('Insira um nome: ')
    idade = input('Insira a idade: ')
    cpf = input('Inseria o CPF: ')

    # instancia o objeto da classe pessoa
    usuario = Pessoa(nome, idade, cpf)

    # exibe os dados na tela
    print(f'Nome: {usuario.nome}.')

    # FIXME: repare que o programa não consegue acessar diretamente os atributos 'idade' e 'cpf', pois os mesmos estão protegidos.
    print(f'Idade: {usuario.idade}.')
    print(f'CPF: {usuario.cpf}.')