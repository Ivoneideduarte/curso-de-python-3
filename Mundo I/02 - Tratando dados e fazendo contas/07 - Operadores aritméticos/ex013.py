# DESAFIO 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

nome = input('Informe seu nome: ')
salario = float(input('Olá, {}! Me informe o valor do seu salário: R$'.format(nome)))
novo = salario + (salario * 15 / 100)
print('Seu salário é R${:.2f} e com o novo reajuste de 15% de acréscimo passou a ser R${:.2f}'.format(salario, novo))
