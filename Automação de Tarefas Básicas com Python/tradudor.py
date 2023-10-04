# tradutor de texto automático usando translate
from traslate import Translator
#criando instancia
tralator = Translator(to_lang="pt")
#solicitando as usuario que escreva o texto
texto = input("Digite o texto que deseja traduzir:")
#traduzindo o texto para portugues
traduzido = tralator.translate(texto)
#mostrando o texto traduzido
print('O texto traduzido é:' + traduzido)

