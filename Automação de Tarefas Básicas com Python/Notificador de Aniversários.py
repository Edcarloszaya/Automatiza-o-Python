#notifucador de aniversários
import datetime

#cria a lista de datas de aniversário
aniversarios = [
    {'nome': 'Joaquim','data_nasc': datetime.date(1999, 1, 1)},
    {'nome': 'carlos','data_nasc': datetime.date(1997, 8,  20)},
    {'nome': 'maria','data_nasc': datetime.date(1994, 3, 15)},
    {'nome': 'ana','data_nasc': datetime.date(1996, 10, 3)},
    {'nome': 'pedro','data_nasc': datetime.date(1998, 4, 11)},
]

# cria funcao para verificar a data de aniversário
def verificar_aniversario_hoje():
    hoje = datetime.date.today()
    aniversarios_hoje = [
       aniversario for aniversario in aniversarios
       if aniversario['data_nasc'].month == hoje.month
       and aniversario['data_nasc'].day == hoje.day
   ]
    return aniversarios_hoje

#chama a funcao e exibe os aniversário
aniversarios_hoje = verificar_aniversario_hoje()
if aniversarios_hoje:
    print(f'Aniversário de {aniversarios_hoje[0]["nome"]}!')
    for aniversario in aniversarios_hoje:
        print(f'{aniversario["nome"]} nasceu em {aniversario["data_nasc"]}')
else:
    print('Nenhum aniversário de hoje!')