'''
Programador: Alex Machado Ribeiro
Programa: Listar Programas
Objetivo: listar todos os programas instalados no PC.
'''

# NOTE: precisa instalar o pacote winapps: pip install winapps

import winapps

for item in winapps.list_installed():
    print(f'Nome do programa: {item.name}.')
    print(f'Versão do programa: {item.version}.')
    print(f'Data da instalação: {item.install_date}.')
    print(f'Data da publicação: {item.publisher}.')
    print(f'Local de desinstalação: {item.uninstall_string}.')
    print('_'*30)