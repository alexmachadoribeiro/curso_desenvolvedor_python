'''
Programador: Alex Machado Ribeiro
Programa: Associação entre Classes
Objetivo: trabalhar com associação entre duas classes.
'''

# NOTE: As classes se relacionam, mas podem existir independentemente uma da outra.

# criando classe aluno
class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.cursos_inscritos = []  # Lista para armazenar os cursos associados ao aluno

    def inscrever_curso(self, curso):
        if curso not in self.cursos_inscritos:
            self.cursos_inscritos.append(curso)
            curso.adicionar_aluno(self)  # Associa o aluno ao curso

    def listar_cursos(self):
        lista = []
        for curso in self.cursos_inscritos:
            lista.append(curso.nome)
        return lista

# criando classe curso
class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos_inscritos = []  # Lista para armazenar os alunos associados ao curso

    def adicionar_aluno(self, aluno):
        if aluno not in self.alunos_inscritos:
            self.alunos_inscritos.append(aluno)
            aluno.inscrever_curso(self)  # Associa o curso ao aluno

    def listar_alunos(self):
        lista = []
        for aluno in self.alunos_inscritos:
            lista.append(aluno.nome)

# programa principal
if __name__ == '__main__':
    # instanciando aluno 1
    aluno1 = Aluno('Fulano', '1001')

    # inserindo dados do aluno 2
    nome = input('Informe o nome do aluno: ')
    matricula = input('Informe o número da matricula: ')

    # instanciando aluno 2 e curso
    aluno2 = Aluno(nome, matricula)
    curso = Curso('Desenvolvedor Python')

    # associando alunos ao curso
    aluno1.inscrever_curso(curso)
    aluno2.inscrever_curso(curso)

    # saída de dados
    print(f'Aluno {aluno1.nome} de matrícula {aluno1.matricula} está inscrito no curso {aluno1.listar_cursos()}')
    print(f'Aluno {aluno2.nome} de matrícula {aluno2.matricula} está inscrito no curso {aluno2.listar_cursos()}')