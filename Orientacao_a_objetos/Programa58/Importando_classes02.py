'''
Programador: Alex Machado Ribeiro
Programa: Importando mais de uma classe
Objetivo: como importar várias classes de um único módulo.
'''

# importando várias classes do método
# NOTE: eu consigo importar uma única classe ou mais de um módulo inteiro
from Classes import Pessoa, Animal

# entrada de dados
nome = input('Informe o nome da pessoa: ')

# instancia o objeto pessoa
usuario = Pessoa(nome)

# exibe o nome da pessoa na tela
print(usuario.falar())

# NOTE: agora, com a classe animal também importada junto com a classe pessoa, consigo instanciar o objeto e acessar seus atributos e métodos.
pet = Animal('Cachorro', 'Rex')
print(pet.expressar())

# FIXME: por outro lado, não é possível ainda instanciar um objeto da classe veidulo, pois ela não foi importada do módulo.
automovel = Veiculo('Carro', 'Palio', 'Fiat')
print(automovel.exibir())