'''
Programador: Alex Machado Ribeiro
Programa: Construtor
Objetivo: trabalhar com construtor de uma classe.
'''

# NOTE: o método construtor é o método responsável por instanciar o objeto.
# Ao programar o método, você indica quais atributos deverão obrigatoriamente inicializar com a instância do objeto.
# Em Python, só é possível ter um único método construtor, ao contrário de outras linguagens de programação.

# ANCHOR: classe pessoa
class Pessoa:
    # método construtor
    # NOTE: o método construtor sempre é inicializado com a palavra reservada '__init__' (dois underscores, palavra init e dois underscores).
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

# ANCHOR: programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe um nome: ')
    idade = input('Informe a idade: ')
    cpf = input('Informe o CPF: ')

    # instancia objeto
    # NOTE: ao programar um método construtor, é obrigatório repassar os atributos da classe na instância do objeto.
    usuario = Pessoa(nome, idade, cpf)

    # exibe os atributos do objeto
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'CPF: {usuario.cpf}.')