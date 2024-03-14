'''
Programador: Alex Machado Ribeiro
Programa: Classe
Objetivo: criar uma classe e instanciar um objeto.
'''

# NOTE: O Paradigma da Orientação a Objetos (POO) é o mais usado para o desenvolvimento de Sistemas Web completos.
# Sua adoção se deve ao fato de facilitar a manutenção do código.
# Cada classe possui atributos e/ou métodos. Os atributos definem características, enquanto os métodos definem ações.
# Um objeto é uma representação de uma classe dentro do programa. Posso criar quantos objetos da mesma classe quiser.
# Isso evita a criação de várias variáveis para representar o mesmo tipo de característica de pessoas diferentes, por exemplo.

# ANCHOR: classe Pessoa
class Pessoa:
    # atributos
    # NOTE: os atributos definem as características que o objeto terá
    nome = 'Fulano de Tal'
    profissao = 'Programador'
    idade = 39

# NOTE: caso a classe e o programa a ser executado estejam no mesmo arquivo, se faz necessário a criação da estrutura if abaixo.

# ANCHOR: programa principal
if __name__ == '__main__':
    # instanciando um objeto do tipo pessoa
    # NOTE: instanciar é o mesmo que criar. Um objeto é uma representação da classe no programa
    usuario = Pessoa()

    # exibe os atributos do objeto do tipo pessoa
    # NOTE: para exibir os atributos do objeto, chama o nome do objeto, seguido do ponto, e depois o atributo que deseja exibir
    print(f'Nome da pessoa: {usuario.nome}.')
    print(f'Profissão da pessoa: {usuario.profissao}.')
    print(f'Idade da pessoa: {usuario.idade}.')