#monitor de uso de espaço em disco em python basico da pra melhorar ele colocando funcoes
import psutil
import time

# Função para monitorar o uso de espaço em disco em um diretório específico
def monitorar_diretorio(diretorio):
    disco = psutil.disk_usage(diretorio)
    espaco_total = disco.total / (1024 ** 3)
    espaco_usado = disco.used / (1024 ** 3)
    espaco_livre = disco.free / (1024 ** 3)

    # Mostra os valores do espaco em disco
    print(f'espaco total em Disco {diretorio}: {espaco_total:.2f} GB')
    print(f'espaco usado em Disco {diretorio}: {espaco_usado:.2f} GB')
    print(f'espaco livre em Disco {diretorio}: {espaco_livre:.2f} GB')
    print('-' * 30)

# Função principal para monitorar vários diretórios
def monitoras_espaco_em_disco(diretorios,limite_max):
    contador = 0 # Contador de diretórios monitorados

    while contador < limite_max:
        for diretorio in diretorios:
            monitorar_diretorio(diretorio)

            contador += 1

        if contador < limite_max:
            time.sleep(10)

# diretórios a serem monitorados
diretorios = ['C:\\', 'D:\\', 'E:\\']

#numero maximo de vericacoes
limite_max = 3

#chama a função principal
monitoras_espaco_em_disco(diretorios,limite_max)

'''
#espera 10 segundos
time.sleep(10)
# chama a função principal de novo
monitoras_espaco_em_disco(diretorios, limite_max)

'''