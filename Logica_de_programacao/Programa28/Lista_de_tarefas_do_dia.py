'''
Programador: Alex Machado Ribeiro
Programa: Lista de tarefas do dia
Objetivo: usuário cria a sua própria lista.
'''

# importa biblioteca
import os

print('-----LISTA DE TAREFAS-----\n')

# declarando o array
tarefas = []

# insere uma atividade até o usuário apertar Enter com o campo em branco
while True:
    atividade = input('Insira uma atividade a ser realizada durante o dia, ou dê enter com o campo em branco para sair: ')

    # verifica se o valor está vazio ou não
    if atividade != '':
        tarefas.append(atividade)
        continue
    else:
        break

# limpa console
os.system('cls')

print('-----LISTA DE TAREFAS DO DIA-----\n')

# exibe a lista de tarefas
for i in range(len(tarefas)):
    print(f'{i + 1}ª tarefa do dia: {tarefas[i]}.')

# finaliza o programa
print('\nFIM!')