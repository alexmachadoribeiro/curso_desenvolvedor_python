'''
Programador: Alex Machado Ribeiro
Programa: Métodos Especiais
Objetivo: trabalhar com métodos especiais do Python.
'''

# criando a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # métodos especiais
    # NOTE: a função str() serve para retornar representações de valores que sejam legíveis para as pessoas.
    def __str__(self):
        return f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.'

    # NOTE: a função repr() é para gerar representações que o interpretador Python consegue ler (ou levantará uma exceção SyntaxError, se não houver sintaxe equivalente).
    def __repr__(self):
        return f'Pessoa("{self.nome}", "{self.idade}")'

# programa principal
if __name__ == '__main__':
    # entrada de dados.
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))

    # instancia o objeto
    usuario = Pessoa(nome, idade)

    # saída de dados.
    print(str(usuario))
    print(repr(usuario))