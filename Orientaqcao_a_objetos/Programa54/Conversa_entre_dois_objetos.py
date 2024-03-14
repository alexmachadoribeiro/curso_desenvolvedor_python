'''
Programador: Alex Machado Ribeiro
Programa: Conversa Entre Dois Objetos
Objetivo: montar um diálogo entre dois objetos.
'''

# classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    # métodos
    def cumprimentar(self):
        return f'Ola, eu sou um {self.profissao} e meu nome é {self.nome}. E o seu?'

    def responder(self, nome):
        return f'Olá {nome}. Meu nome é {self.nome} e sou um {self.profissao}. Muito prazer.'

# programa principal
if __name__ == '__main__':
    # entrada de dados do usuário
    nome = input('Informe seu nome: ')
    idade = input('Informe sua idade: ')
    profissao = input('Informe sua profissão: ')

    # instancia dos objetos
    usuario = Pessoa(nome, idade, profissao)
    npc = Pessoa('Emmanuelle', 18, 'Programadora')

    # conversa entre os objetos
    print(npc.cumprimentar())
    print(usuario.responder(npc.nome))