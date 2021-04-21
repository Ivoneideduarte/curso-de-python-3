# DESAFIO 14:  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Informe a temperatura em ºC: '))
f = (c * 9/5) + 32
print('A temperatude de {:.1f}ºC corresponde a {}ºF'.format(c, f))