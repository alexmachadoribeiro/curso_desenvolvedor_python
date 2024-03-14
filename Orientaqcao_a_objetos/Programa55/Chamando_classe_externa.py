'''
Programador: Alex Machado Ribeiro
Programa: Classe Externa
Objetivo: instanciar um objeto de uma classe de outro arquivo.
'''

# importando módulo da classe
# NOTE: o nome do módulo é o nome do arquivo
import Modulo

# entrada de dados
nome = input('Informe seu nome: ')
profissao = input('Informe a sua profissão: ')
requisitos = True

# instanciando objeto
# NOTE: para instanciar objeto de uma classe de um arquivo externo, chame o nome_do_módulo.nome_da_classe() no construtor
usuario = Modulo.Pessoa(nome, profissao)

# saída de dados
print(f'Nome: {usuario.nome}.')
print(f'Profissão: {usuario.profissao}.')

# executando método da classe
usuario.executar_programa(requisitos)