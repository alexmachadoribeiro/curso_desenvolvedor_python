'''
Programador: Alex Machado Ribeiro
Programa: Classe Externa
Objetivo: instanciar um objeto de uma classe de outro arquivo.
'''

# importando classe
# NOTE: usando 'from Modulo import Classe', você importa diretamente a classe, e não precisa mencionar o nome do módulo na instância do objeto
from Modulo import Pessoa

# entrada de dados
nome = input('Informe seu nome: ')
profissao = input('Informe a sua profissão: ')
requisitos = False

# instanciando objeto
usuario = Pessoa(nome, profissao)

# saída de dados
print(f'Nome: {usuario.nome}.')
print(f'Profissão: {usuario.profissao}.')

# executando método da classe
usuario.executar_programa(requisitos)