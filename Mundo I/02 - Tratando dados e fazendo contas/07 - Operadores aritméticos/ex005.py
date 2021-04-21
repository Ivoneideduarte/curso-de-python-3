# DESAFIO 05: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número: '))
sucessor = numero + 1
antecessor = numero - 1
print('O sucessor de {} é {} e o antecessor de {} é {}'.format(numero, sucessor, numero,antecessor))