'''
Programador: Alex Machado Ribeiro
Programa: Adicionar ao Dicionário
Objetivo: inserir uma nova chave no dicionário.
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

# insere nova chave
dados_usuario['Cidade'] = input('Informe a cidade onde mora: ')
dados_usuario['Genero'] = input('Informe o gênero com o qual se identifica: ')

# novo dicionário
print(dados_usuario)