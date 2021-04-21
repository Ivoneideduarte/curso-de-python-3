# DESAFIO 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

'''
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo)) #Pega o ângulo e converte pra radianos e calcula o seno
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, tan))
'''

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(angulo)) #Pega o ângulo e converte pra radianos e calcula o seno
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('O ângulo de {} tem SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(angulo, cos))
print('O ângulo de {} tem TANGENTE de {:.2f}'.format(angulo, tan))