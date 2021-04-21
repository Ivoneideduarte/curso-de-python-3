# DESAFIO 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# Inicializando as variáveis com valor zero
soma = 0
cont = 0
for c in range(1, 7): # 1 até 6
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0: # Número par
        soma += num
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

