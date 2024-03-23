# importa biblioteca
import time

# classes

# NOTE: herança múltipla é quando uma única subclasse herda atributos e métodos de duas superclasses, ou mais.

# superclasse 1
class Pai:
    nome = 'Fulano'
    raca = 'Caucasiano'
    temperamento = 'Calmo'
    profissao = 'Programador'

    def executar_acao(self):
        print('Executar programa...')
        time.sleep(2)
        print('Executando programa...')
        time.sleep(2)
        print('Programa executado com sucesso!')

# superclasse 2
class Mae:
    olhos = 'Verdes'
    cor_cabelo = 'Ruivo'
    peso = 70
    altura = 1.8

    def exibir_dados(self):
        print(f'Olhos: {self.olhos}.')
        print(f'Cor do cabelo: {self.cor_cabelo}.')
        print(f'Peso: {self.peso} kg.')
        print(f'Altura: {self.altura} metros.')

# subclasse
class Filho(Pai, Mae):
    def exibir_dados(self):
        print(f'Nome: {self.nome}.')
        print(f'Raça: {self.raca}.')
        print(f'Temperamento: {self.temperamento}.')
        print(f'Profissão: {self.profissao}.')
        super().exibir_dados() # polimorfismo

# NOTE: Benefícios da herança múltipla:
# Reutilização de Código: Evita a repetição de código ao permitir que uma classe herde comportamentos e atributos de várias classes.
# Extensibilidade: Novas funcionalidades podem ser facilmente adicionadas a um programa.
# Modularidade: Separação clara de funcionalidades em diferentes classes.

# NOTE: Desafios da Múltipla Herança:
# Ambiguidade: Se duas superclasses tiverem métodos com o mesmo nome, pode haver ambiguidade sobre qual método a subclasse deve herdar.
# Complexidade: A manutenção pode se tornar desafiadora, especialmente quando há várias cadeias de herança.
# Problema do Diamante: Um desafio clássico na múltipla herança, ocorre quando uma classe herda de duas classes que têm uma superclasse comum.