# importa a biblioteca abc para trabalhar com as classes abstratas
# NOTE: é necessário a importação da biblioteca abc para criar as classes abstratas
from abc import ABC, abstractmethod

# cria uma classe abstrata
# NOTE: uma classe abstrata em Python é basicamente uma classe que herda a classe ABC.
class Conta(ABC):

    # métodos abstratos
    # NOTE: os métodos abstratos não precisam ser programados na classe abstrata, apenas mecionados com a anotação @abstractmethod, para que sua subclasse tenha obrigatoriamente seus métodos.
    @abstractmethod
    def consultar_dados(self):
        pass

    @abstractmethod
    def fazer_deposito(self):
        pass

    @abstractmethod
    def fazer_saque(self):
        pass

# subclasse da classe abstrata
# NOTE: em outras linguagens, criar uma subclasse de uma classe abstrata é o mesmo que implementar uma interface.
# Em Java, por exemplo, seria public class ContaCorrente implements Conta
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

    # TODO: uma subclasse de uma classe abstrata não pode ficar sem os métodos da superclasse.