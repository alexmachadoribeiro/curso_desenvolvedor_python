'''
Programador: Alex Machado Ribeiro
Programa: YouTube downloader
Objetivo: baixar um vídeo do youtube.
'''

# NOTE: precisa instalar o pacote pytube: pip install pytube

from pytube import YouTube
from pytube.cli import on_progress # barra de progresso

# informa o link do vídeo
link_do_video = input('Informe o link do vídeo: ')

# mensagem de espera
print('Baixando vídeo...')

# NOTE: após a mensagem de baixando o vídeo, o progresso irá demorar um pouco para aparecer. Paciência...

# captura o caminho do vídeo do youtube e exibe a barra de progresso
yt = YouTube(link_do_video, on_progress_callback=on_progress)

# pega a maior resolução possível
video_stream = yt.streams.get_highest_resolution()

# baixa o vídeo no diretório do projeto
video_stream.download()

# mensagem final a ser exibida
print('Download completo!')