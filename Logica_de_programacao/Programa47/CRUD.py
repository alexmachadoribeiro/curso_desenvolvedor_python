'''
Programador: Alex Machado Ribeiro
Programa: CRUD
Objetivo: CRUD com Python.
'''

# ANCHOR: funções
# função menu
def mostrar_menu():
    print('\n1 - Adicionar novo nome.')
    print("2 - Listar nomes.")
    print('3 - Pesquisar por um nome.')
    print('4 - Atualizar nome.')
    print('5 - Deletar um nome.')
    print('6 - Ordenar a lista em ordem alfabética.')
    print('7 - Finalizar programa.')

# ANCHOR: programa principal
# lista de nomes
nomes = ['Fulano', 'Cicrano', 'Beltrano', 'João', 'Maria', 'José']

while True:
    # mostra menu de opções
    mostrar_menu()

    # obtém resposta do usuário
    opcao = input('Informe a opção desejada: ')

    # verifica a opção escolhida
    if opcao == '1':
        # adiciona novo nome na lista
        novo_nome = input('Informe o nome a ser adicionado na lista: ')
        nomes.append(novo_nome)
        print(f'"{novo_nome}" adicionado com sucesso.')
        continue
    elif opcao == '2':
        # exibe a lista na tela
        for i in range(len(nomes)):
            print(f'{i + 1} - {nomes[i]}')

        continue
    elif opcao == '3':
        # pesquisa por um nome
        pesquisa_nome = input('Informe o nome que deseja pesquisar: ')
        resultado = pesquisa_nome in nomes

        if resultado == True:
            print(f'A pesquisa retornou {nomes.count(pesquisa_nome)} resultados.')
        else:
            print('A pesquisa não encontrou nenhum resultado.')

        continue
    elif opcao == '4':
        # atualiza um índice
        posicao = int(input('Informe a posição do nome que deseja trocar: '))
        print(f'Nome a ser alterado: {nomes[posicao - 1]}.')
        nome_antigo = nomes[posicao - 1]
        nomes[posicao - 1] = input('Informe o novo nome: ')
        print(f'{nome_antigo} alterado para {nomes[posicao - 1]} com sucesso.')
        continue
    elif opcao == '5':
        # deleta um nome
        posicao = int(input('Informe a posição do nome que deseja deletar:'))
        deletar = input(f'Deseja deletar {nomes[posicao - 1]} da lista (s/n)?')

        if deletar == 's':
            del(nomes[posicao - 1])
            print('Nome deletado com sucesso.')
            continue
        else:
            print('Operação cancelada.')
            continue
    elif opcao == '6':
        # ordena a lista em ordem alfabética
        nomes.sort()
        print('Lista ordenada com sucesso.')
        continue
    elif opcao == '7':
        # sai do programa
        print('Até mais...')
        break
    else:
        print('Opção inválida.')