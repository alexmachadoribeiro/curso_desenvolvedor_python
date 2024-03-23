'''
Programador: Alex Machado Ribeiro
Programa: Dataclasses
Objetivo: trabalhar com dataclass.
'''

# NOTE: Dataclasses podem ser vistas como uma extensão das classes normais do python.
# O objetivo é reduzir a repetição e o custo de códigos que são comuns na comunidade.

# importando o dataclass
from dataclasses import dataclass

# NOTE: a anotação @dataclass permite inserir atributos e tipá-los.
@dataclass
class Pessoa:
    # atributos
    nome: str
    idade: int
    altura: float

# programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe sua idade: '))
    altura = float(str(input('Informe sua altura em metros: ').replace(',', '.')))

    # instanciando o objeto
    # NOTE: observe que ainda há a necessidade de repassar os atributos para o construtor, mesmo não tendo inserido na classe.
    usuario = Pessoa(nome, idade, altura)

    # saída de dados
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'Altura: {usuario.altura} metros.')