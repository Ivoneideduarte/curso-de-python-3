# DESAFIO 07: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

nome = input('Digite o seu nome: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2)/2
print('Olá, {}! Sua média é {:.1f}'.format(nome, media))
