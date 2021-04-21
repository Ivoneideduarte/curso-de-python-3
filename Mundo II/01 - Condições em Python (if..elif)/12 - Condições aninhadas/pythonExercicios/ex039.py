# DESAFIO 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

atual = date.today().year # Pega o ano atual
genero = int(input('''[ 1 ] Masculino \n[ 2 ] Femenino \nInforme o seu gênero: '''))

nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18 and genero == 1:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade == 18 or genero == 2:
    print('Você não é OBRIGADA a se alistar!')
elif idade < 18 and genero == 1:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18 and genero == 1:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
