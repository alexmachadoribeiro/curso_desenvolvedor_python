# importa biblioteca
import time

# classe pessoa
class Pessoa:
    # construtor
    def __init__(self, nome, profissao):
        self.nome = nome
        self.profissao = profissao

    def executar_programa(self, requisitos):
        if requisitos == True:
            print('Programando aplicação...')
            time.sleep(2)
            print('Depurando aplicação...')
            time.sleep(2)
            print('Testando aplicação...')
            time.sleep(2)
            print('Gerando executável...')
            time.sleep(2)
            print('Aplicativo criado com sucesso!')
        else:
            print('Não é possível trabalhar na aplicação.')