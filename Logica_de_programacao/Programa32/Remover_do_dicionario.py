'''
Programador: Alex Machado Ribeiro
Programa: Remover do Dicionário
Objetivo: remover uma chave do dicionário.
'''

# dicionário
dados_usuario = {
    'Nome':'Alex Machado',
    'Idade':39,
    'Empresa':'SENAI',
    'Profissao':'Programador'
}

# saída de dados
print(dados_usuario)

# remove uma chave do dicionário
dados_usuario.pop(input('Deseja excluir qual chave? Nome, Idade, Empresa ou Profissão? '), None)

# NOTE: O 'None' serve para que a mensagem de erro 'KeyError' não apareça devido a remoção de uma chave inexistente.

# novo dicionário
print(dados_usuario)