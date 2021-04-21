# DESAFIO 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''
from random import randint
sorteio = randint(0, 5)
num = int(input('Adivinhe o número: '))
print('O número sorteado foi {} e a sua aposta foi {}'.format(sorteio, num))

if num == sorteio:
    print('Você VENCEU!')
else:
    print('Você PERDEU!')
'''

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador 'PENSAR'
#print('Pensei no número {}'.format(computador))
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
