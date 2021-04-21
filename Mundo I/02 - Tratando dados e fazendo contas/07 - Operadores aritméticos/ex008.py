# DESAFIO 08: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

valorMetro = int(input('Digite um valor em metros: '))
centimetros = valorMetro * 100
milimetros = valorMetro * 1000
print('O valor {} em metros equivale em centimetros a {} e em milimetros a {}'.format(valorMetro, centimetros, milimetros))