'''
Programador: Alex Machado Ribeiro
Programa: Classes Abstratas
Objetivo: trabalhar com classes abstratas.
'''

# importa classe abstrata do módulo.
# REVIEW: para fins de demonstração, iremos importar apenas a classe abstrata.
from Modulo import Conta

# instancia objeto da classe Conta
# FIXME: o comando de instancia do objeto irá retornar um erro, uma vez que não se pode instanciar objetos de classes abstratas.
conta = Conta()

# chama os métodos da classe
# FIXME: os métodos abaixo não irão funcionar, já que o objeto não pÔde ser instanciado.
conta.consultar_dados()
conta.fazer_deposito()
conta.fazer_saque()