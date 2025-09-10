import PyPDF2
import os 
from tkinter.filedialog import askdirectory

merger = PyPDF2.PdfMerger()
path = askdirectory (title = "Selecione a pasta com os arquivos pdf")
lista_arquivos = os.listdir(path)
lista_arquivos.sort()
for arquivo in lista_arquivos:
    print(arquivo)

for arquivo in lista_arquivos:
    if arquivo.endswith('.pdf'):
        merger.append(f"{path}/{arquivo}")
merger.write(f"{path}/Arquivo_mesclado.pdf")
merger.close()        