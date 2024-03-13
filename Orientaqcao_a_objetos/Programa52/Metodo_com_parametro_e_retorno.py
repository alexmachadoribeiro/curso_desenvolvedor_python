'''
Programador: Alex Machado Ribeiro
Programa: Métodos com parâmetro e retorno
Objetivo: trabalhar com os parâmetros e retornos de métodos de uma classe.
'''

# classe pessoa
class Pessoa:
    # atributos
    nome = 'Fulano de Tal'
    profissao = 'Programador'
    salario_bruto = 5000

    # método
    def receber_salario(self, descontos):
        return self.salario_bruto - descontos

# programa principal
if __name__ == '__main__':
    # instancia o objeto pessoa
    usuario = Pessoa()

    # exibe os atributos da pessoa
    print(f'Nome: {usuario.nome}.')
    print(f'Profissão: {usuario.profissao}.')
    print(f'Salário bruto: R$ {usuario.salario_bruto:,.2f}.')

    # informe o valor dos descontos
    descontos = float(input('Informe o valor dos desontos: R$ '))

    # exibe na tela o salário líquido
    print(f'Salário líquido: R$ {usuario.receber_salario(descontos):,.2f}')