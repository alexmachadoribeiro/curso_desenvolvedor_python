'''
Programador: Alex Machado Ribeiro
Programa: IMC
Objetivo: criar um programa que recebe do usuário o nome, altura e peso, calcule o IMC do usuário, e retorne um diagnóstico.
'''

# entrada de dados
nome = input('Informe o seu nome: ')
# NOTE: é necessário informar um valor em string para substituir a vírgula informada pelo usuário por ponto, para que possa ser calculado como um float
peso = str(input('Informe o seu peso em kg: ')).replace(',','.')
altura = str(input('Informe a sua altura em metros: ')).replace(',','.')

# calcula o IMC do usuário dividindo o peso pela altura ao quadrado
# NOTE: o peso e a altura nesse momento estão como string. É necessário converter para float para poder calcular o imc
imc = float(peso) / float(altura)**2

# NOTE: ** é o operador para potência. Exemplo: variavel**potenciacao

# exibe o valor do imc na tela
# NOTE: variavel:,.numerof para arredondar casas decimais, onde número é o número de casas decimais a serem exibidas
print(f'Valor do IMC: {imc:,.2f}.')

# verifica o imc e retorna o diagnóstico
if imc < 17:
    print(f'{nome} está com anorexia.')
elif imc < 18.5:
    print(f'{nome} está abaixo do peso.')
elif imc < 25:
    print(f'{nome} está no peso ideal.')
elif imc < 30:
    print(f'{nome} está acima do peso.')
elif imc < 35:
    print(f'{nome} está com grau de obesidade I.')
elif imc < 40:
    print(f'{nome} está com grau de obesidade II.')
else:
    print(f'{nome} está com grau de obesidade mórbida.')

# NOTE: elif é a versão 'else if' do Python