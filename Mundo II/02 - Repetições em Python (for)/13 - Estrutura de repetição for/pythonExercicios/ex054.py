# DESAFIO 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
totalMaior = 0
totalMenor = 0

for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade = atual - nasc
    # print('Sua idade é {}'.format(idade))
    if idade >= 21:
        totalMaior += 1
    else:
        totalMenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totalMaior))
print('E também tivemos {} pessoas menores de idade'.format(totalMenor))