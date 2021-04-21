'''
DESAFIO 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
'''

from datetime import date

print('-=' * 18)
print('  Confederação Nacional de Natação ')
print('-=' * 18)
atual = date.today().year # Pega o ano atual
nasc = int(input('\nAno de nascimento: '))
idade = atual - nasc # Calcula a idade do atleta
print('O atleta tem {} anos: '.format(idade))

'''
if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade > 9 and idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade > 14 and idade <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade > 19 and idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
elif idade > 25:
    print('CLASSIFICAÇÃO: MASTER')
'''

if idade <= 9:
    print('CLASSIFICAÇÃO: MIRIM')
elif idade <= 14:
    print('CLASSIFICAÇÃO: INFANTIL')
elif idade <= 19:
    print('CLASSIFICAÇÃO: JÚNIOR')
elif idade <= 25:
    print('CLASSIFICAÇÃO: SÊNIOR')
else:
    print('CLASSIFICAÇÃO: MASTER')
