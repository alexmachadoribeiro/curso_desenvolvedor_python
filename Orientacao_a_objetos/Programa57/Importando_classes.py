'''
Programador: Alex Machado Ribeiro
Programa: Importando mais de uma classe
Objetivo: como importar várias classes de um único módulo.
'''

# importando uma só classe do método
# NOTE: eu consigo importar uma única classe ou mais de um módulo inteiro
from Classes import Pessoa

# entrada de dados
nome = input('Informe o nome da pessoa: ')

# instancia o objeto pessoa
usuario = Pessoa(nome)

# exibe o nome da pessoa na tela
print(usuario.falar())

# FIXME: como só a classe Pessoa foi importada, a classe Animal ficou de fora, e portanto não pode ser instanciada. Com isso, todas as linhas abaixo não funcionam.
pet = Animal('Cachorro', 'Rex')
print(pet.expressar())