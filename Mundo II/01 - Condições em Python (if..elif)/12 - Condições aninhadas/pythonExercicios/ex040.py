'''
DESAFIO 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO
'''

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2

print('Com a nota {:.1f} e {:.1f} sua média é {:.1f}'.format(nota1, nota2, media))

if media < 5:
    print('Você está REPROVADO! com a média {:.1f}'.format(media))
elif media == 5 or media < 7:
    print('Você está de RECUPERAÇÃO! com a média {:.1f}'.format(media))
else:
    print('Você está APROVADO! com a média {:.1f}'.format(media))