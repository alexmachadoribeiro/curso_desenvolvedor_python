# importa a biblioteca abc para trabalhar com as classes abstratas
from abc import ABC, abstractmethod

# cria uma classe abstrata
class Conta(ABC):
    # NOTE: alteramos alguns métodos para receber parâmetros do programa principal.

    # métodos abstratos
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def fazer_deposito(self, valor):
        pass

    @abstractmethod
    def fazer_saque(self, valor):
        pass

# subclasse da classe abstrata
class ContaCorrente(Conta):
    # atributos
    __agencia = 10011
    __saldo = 0.0

    # construtor
    def __init__(self, nome, cpf, conta):
        self.__nome = nome
        self.__cpf = cpf
        self.__conta = conta

    # métodos de acesso get e set
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def conta(self):
        return self.__conta

    @conta.setter
    def conta(self, conta):
        self.__conta = conta

    @property
    def agencia(self):
        return self.__agencia

    @agencia.setter
    def agencia(self, agencia):
        self.__agencia = agencia

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    # métodos da classe abstrata
    # NOTE: todos os métodos da classe abstrata devem ser implementados obrigatoriamente na subclasse.
    def consultar_dados(self):
        print(f'Nome: {self.__nome}.')
        print(f'CPF: {self.__cpf}.')
        print(f'Agência: {self.__agencia}.')
        print(f'Conta: {self.__conta}.')
        print(f'Saldo: R$ {self.__saldo:,.2f}.')

    def fazer_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo

    def fazer_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo