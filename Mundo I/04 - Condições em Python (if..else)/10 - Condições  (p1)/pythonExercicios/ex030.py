# DESAFIO 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Me diga um número inteiro qualquer: '))
resultado = num % 2
#print('O resultado foi {}'.format(resultado))

if  resultado == 0:
    print('O número {} é PAR!'.format(num))
else:
    print('O número {} é ÍMPAR!'.format(num))