# renomiador de arquivo em massa usando o Python
import os

# recebe o caminho da pasta dos arquivos que deseja renomear
pasta= input('digitar o caminho dos arquivos que deseja renomear: ') # caminho da pasta que sera renomeado
pasta_renomeada = input('digitar o caminho da pasta onde sera  renomeada os arquivos: ') # caminho da pasta renomeada
nome_novo = input('digitar o nome do novo arquivo: ') # nome do novo arquivo a ser criador
extensao = input('digitar a extensão do novo arquivo: ') # extensão do novo arquivo

# verifica se a pasta existe
if not os.path.exists(pasta):
    print('Pasta não existe')
    exit()

# renomeia os arquivos da pasta para o novo nome e extensão informado
for contador, nome_arquivo in enumerate(os.listdir(pasta)):
    nome_novo_arquivo = f"{nome_novo}_{contador+1}{extensao}"
    pasta_antiga = os.path.join(pasta, nome_arquivo)
    pasta_nova = os.path.join(pasta_renomeada, nome_novo_arquivo)

# tratamento de erros que podem gera durante o processo
    try:
     os.rename(pasta_antiga, pasta_nova) # renomeia os arquivos
    except FileExistsError:
     print(f'O arquivo {nome_novo} já existe na pasta {pasta_renomeada}')
    except FileNotFoundError:
     print(f' a pasta nao foi encontrada')
    except PermissionError:
     print(f'nao tem permissao para renomear os arquivos')
    except Exception as e:
     print(f'Erro inesperado: {e}')


#mostra quando os arquivos foram renomeados
print(f'Arquivos renomeados com sucesso!')
