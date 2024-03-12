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
# NOTE: com 'del', não há a necessidade de repassar o parâmetro 'None'
del dados_usuario[input('Deseja excluir qual chave? Nome, Idade, Empresa ou Profissão? ')]

# novo dicionário
print(dados_usuario)