'''
Importe o módulo random para gerar elementos aleatórios.
Defina uma lista de caracteres que serão usados para criar a senha. Isso pode incluir letras maiúsculas e minúsculas, números e caracteres especiais.
Defina o comprimento da senha desejada.
Use a função random.choice() para selecionar aleatoriamente elementos da lista de caracteres e construir a senha.
Repita o passo anterior até que a senha atinja o comprimento desejado.
Embaralhe a ordem dos caracteres da senha para aumentar a segurança.
Retorne a senha gerada.

'''
import random

#   lista a ser ussada para gerar a senha
caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
#Defina o comprimento da senha desejada
comprimento = 12
#Use a função random.choice() para selecionar aleatoriamente elementos da lista de caracteres e construir

senha = '' #Crie uma variável para armazenar a senha

for i in range(comprimento): #Repita o passo anterior até que a senha atinja o comprimento desejad
    senha += random.choice(caracteres) #Embaralhe a ordem dos caracteres da senha para aumentar a segurança.

#Retorne a senha gerada
print(senha)
