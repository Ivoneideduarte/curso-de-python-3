# DESAFIO 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(casa, anos, prestacao))
# print('COMPARANDO tem que pagar {} e o mínimo é de {}'.format(prestacao, minimo))

if prestacao <= minimo:
    print('Empréstimo pode ser {}CONCEDIDO{}'.format('\033[1;32m', '\033[m'))
else:
    print('Empréstimo {}NEGADO{}'.format('\033[1;31m', '\033[m'))
