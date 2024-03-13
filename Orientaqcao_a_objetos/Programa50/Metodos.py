'''
Programador: Alex Machado Ribeiro
Programa: Métodos
Objetivo: trabalhar com os métodos de uma classe.
'''

# classe pessoa
class Pessoa:
    # atributos
    nome = 'Fulano de Tal'
    profissao = 'Programador'
    idade = 39

    # método
    # NOTE: métodos são ações do objeto. Podem receber ou não parâmetros (valores dentro dos parênteses) e podem ou não retornar algum valor (comando return).
    # Independente de terem ou não parâmetros, sempre vão ter a palavra reservada 'self' dentro dos parênteses.
    # O 'self' no Python é o equivalente ao 'this' das outras linguagens.
    def apresentar(self):
        print(f'Olá. Meu nome é {self.nome}, trabalho como {self.profissao} e tenho {self.idade} anos.')

# programa principal
if __name__ == '__main__':
    # instancia o objeto pessoa
    usuario = Pessoa()

    # executa a ação (método) do objeto
    usuario.apresentar()