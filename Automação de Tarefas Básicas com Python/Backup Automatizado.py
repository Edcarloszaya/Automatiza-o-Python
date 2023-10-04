# Para criar um backup automatizado em Python
import os
import shutil

# diretorio de origem e destino
diretorio_origem = input("Digite o nome do diretorio de origem: ")
diretorio_destino = input("Digite o nome do diretorio de destino: ")

# lista os arquivos para o backup
arquivos = os.listdir(diretorio_origem)

# verifica se o diretorio de destino existe
if not os.path.exists(diretorio_destino):
    os.makedirs(diretorio_destino)  # cria o diretorio de destino

#cria backup
for arquivo in arquivos:
    caminho_origem = os.path.join(diretorio_origem, arquivo)
    caminho_destino = os.path.join(diretorio_destino, arquivo)


    try:
        shutil.copy2(caminho_origem, caminho_destino)
        print(f'BACKUP DO ARQUIVO {arquivo} REALIZADO!')

    except IOError as e:
        print(f"Erro ao copiar o arquivo {arquivo}: {str(e)}")
    except FileNotFoundError as e:
        print(f"Arquivo {arquivo} não encontrado: {str(e)}")
    except PermissionError as e:
        print(f"Permissão negada ao copiar {arquivo}: {str(e)}")
    except IsADirectoryError as e:
        print(f"{arquivo} é um diretório e não pode ser copiado: {str(e)}")
    except Exception as e:
        print(f"Erro ao copiar o arquivo {arquivo}: {str(e)}")





