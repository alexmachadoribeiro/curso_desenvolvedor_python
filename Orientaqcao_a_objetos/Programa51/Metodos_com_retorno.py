'''
Programador: Alex Machado Ribeiro
Programa: Métodos com retorno
Objetivo: trabalhar com os retornos de métodos de uma classe.
'''

# ANCHOR: classe pessoa
class Pessoa:
    # atributos
    nome = 'Fulano de Tal'
    peso = 80
    altura = 1.80

    # método
    def calcular_imc(self):
        # NOTE: o comando return é usado em métodos para retornar algum valor para ser usado no programa principal, como a função de saída de dados ou para enviar o valor para alguma variável.
        return self.peso / self.altura ** 2

# ANCHOR: programa principal
if __name__ == '__main__':
    # instancia o objeto pessoa
    usuario = Pessoa()

    # exibe os atributos na tela
    print(f'Nome: {usuario.nome}.')
    print(f'Peso: {usuario.peso} kg.')
    print(f'Altura: {usuario.altura} metros.')

    # exibe o retorno do método
    print(f'IMC: {usuario.calcular_imc():,.2f}.')