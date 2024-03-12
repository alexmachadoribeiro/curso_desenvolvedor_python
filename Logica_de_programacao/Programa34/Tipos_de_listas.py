'''
Programador: Alex Machado Ribeiro
Programa: Tipos de listas
Objetivo: identificar os tipos de listas.
'''

# declaração de listas
lista = ['Fulano','Cicrano','Beltrano']
tupla = ('Brasília','São Paulo','Rio de Janeiro')
dicionario = {
    'Nome':'Fulano de Tal',
    'Profissao':'Programador',
    'Genero':'Masculino'
}

# exibição dos tipos de lista na tela
# NOTE: a função 'type()' também pode ser utilizada para identificar os tipos de listas
print(type(lista))
print(type(tupla))
print(type(dicionario))