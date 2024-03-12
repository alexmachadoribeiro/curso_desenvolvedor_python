'''
Programador: Alex Machado Ribeiro
Programa: Dicionário
Objetivo: estrutura de dados similar ao JSON do JavaScript.
'''

# NOTE: Estrutura de um dicionário: variavel = {
#         'chave1':'dado1',
#         'chave2','dado2'
#     }
# é uma estrutura de dados parecida com o JSON do JS.
dados_usuario = {
    'Nome':'Alex Machado',
    'Idade':39,
    'Empresa':'SENAI',
    'Profissao':'Programador'
}

# NOTE: Acesso aos dados forma 1: variavel['chave']
print(f"Nome do usuário: {dados_usuario['Nome']}.")
print(f"Idade: {str(dados_usuario['Idade'])}.")

# NOTE: forma 2: variavel.get('chave') na forma 2, caso a chave não exista, ele não irá retornar erro.
print(f"Empresa: {dados_usuario.get('Empresa')}.")
print(f"Profissão: {dados_usuario.get('Profissao')}.")