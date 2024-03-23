# superclasse ou classe-pai
# NOTE: a superclasse ou classe-pai é uma classe como qualquer outra.
# Porém, seu objetivo é guardar atributos e métodos que serão comuns para outras classes.
class Pessoa:
    def __init__(self, nome, email, endereco):
        self.__nome = nome
        self.__email = email
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

# NOTE: subclasses ou classes-filhas são classes que irão herdar atributos e métodos de outras classes.
# O objetivo é reaproveitar o código, para que não seja necessário redigitar o mesmo código de novo.
# Funciona assim: Subclasse(Superclasse).
# Isso é equivalente ao Superclasse extends Subclasse de outras linguagens.

# subclasse ou classe-filha pessoa física
class PessoaFisica(Pessoa):
    # conlstrutor
    def __init__(self, nome, email, endereco, cpf, cargo):
        super().__init__(nome=nome, email=email, endereco=endereco) # polimorfismo
        self.__cpf = cpf
        self.__cargo = cargo

    # NOTE: polimorfismo é uma das principais características da orientação a objetos.
    # Ela serve para que um método herdado de uma superclasse seja reutilizado, porém adotando um coportamento diferente.
    # Utilizamos o método super() para isso.

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo

# NOTE: várias classes podem herdar atributos e métodos de uma mesma superclasse.

# subclasse ou classe-filha pessoa jurídica
class PessoaJuridica(Pessoa):
    def __init__(self, nome, email, endereco, cnpj, setor):
        super().__init__(nome=nome, email=email, endereco=endereco)
        self.__cnpj = cnpj
        self.__setor = setor

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self.__cnpj = cnpj

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

# NOTE: diferente da maioria das linguagens de programação orientadas a objetos, Python suporta herança múltipla.