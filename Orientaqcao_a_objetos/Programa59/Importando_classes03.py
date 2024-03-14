'''
Programador: Alex Machado Ribeiro
Programa: Importando mais de uma classe
Objetivo: como importar várias classes de um único módulo.
'''

# importando várias classes do método
# NOTE: usando o asterístico (*) consigo importar todas as classes do módulo de uma vez só.
from Classes import *

# entrada de dados
nome = input('Informe o nome da pessoa: ')

# instancia o objeto pessoa
usuario = Pessoa(nome)

# exibe o nome da pessoa na tela
print(usuario.falar())

# NOTE: agora consigo importar todas as classes do módulo.

# classe animal instanciada
pet = Animal('Cachorro', 'Rex')
print(pet.expressar())

# classe veiculo instanciada
automovel = Veiculo('Carro', 'Palio', 'Fiat')
print(automovel.exibir())