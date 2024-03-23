# NOTE: consigo criar várias classes em um único arquivo.

# ANCHOR: classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome):
        self.nome = nome

    # método
    def falar(self):
        return f'Olá, me chamo {self.nome} e eu sou uma pessoa.'

# ANCHOR: classe animal
class Animal:
    # construtor
    def __init__(self, tipo, nome):
        self.tipo = tipo
        self.nome = nome

    # método
    def expressar(self):
        return f'Oi, me chamo {self.nome} e sou um {self.tipo}.'

# ANCHOR: classe veiculo
class Veiculo:
    # construtor
    def __init__(self, tipo, modelo, fabricante):
        self.tipo = tipo
        self.modelo = modelo
        self.fabricante = fabricante

    # método
    def exibir(self):
        return f'OLá, eu sou um {self.tipo}, um modelo {self.modelo} do fabricante {self.fabricante}.'