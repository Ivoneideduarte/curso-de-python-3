# DESAFIO 04: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

valor = input('Digite algo: ')

print('Seu tipo primitivo é: {}'.format(type(valor)))
print('Só tem espaços? {}'.format(valor.isspace()))
print('É um número? {}'.format(valor.isnumeric()))
print('É alfabético? {}'.format(valor.isalpha()))
print('É alfanúmerico? {}'.format(valor.isalnum()))
print('Está em maiúsculas? {}'.format(valor.isupper()))
print('Está em minúsculas? {}'.format(valor.islower()))
print('Está capitalizada? {}'.format(valor.istitle())) #Letras maiúculas misturadas com minúsculas


