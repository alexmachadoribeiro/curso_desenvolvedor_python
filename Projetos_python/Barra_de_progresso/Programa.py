'''
Programador: Alex Machado Ribeiro
Programa: Barra de Progresso
Objetivo: simular uma barra de progresso no console.
'''

# NOTE: precisa instalar o pacote tqdm: pip install tqdm

from tqdm import tqdm
import time

for i in tqdm(range(100)):
    time.sleep(0.05)