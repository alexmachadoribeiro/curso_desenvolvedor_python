'''
Programador: Alex Machado Ribeiro
Programa: Composição entre Classes
Objetivo: trabalhar com composição entre duas classes.
'''

# NOTE: Uma classe contém outra classe como um de seus campos.

# cria classe endereço
class Endereco:
    # construtor
    def __init__(self, rua, cidade, estado):
        self.rua = rua
        self.cidade = cidade
        self.estado = estado

    # método
    def obter_endereco_completo(self):
        return f"{self.rua}, {self.cidade}, {self.estado}"

# cria classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco  # Composição: Pessoa tem um Endereco

    # método
    def obter_info_pessoal(self):
        return f"{self.nome}, {self.idade} anos, mora em {self.endereco.obter_endereco_completo()}"

# programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    local_moradia = input('Informe onde você mora: ')
    cidade = input('Informe a cidade de seu endereço: ')
    estado = input('Informe o estado de seu endereço: ')

    # instancia objetos endereço e pessoa
    endereco_pessoa1 = Endereco(local_moradia, cidade, estado)
    pessoa1 = Pessoa(nome, idade, endereco_pessoa1)

    # saída de dados
    print(pessoa1.obter_info_pessoal())
    print(pessoa1.endereco.rua)
    print(pessoa1.endereco.cidade)
    print(pessoa1.endereco.estado)