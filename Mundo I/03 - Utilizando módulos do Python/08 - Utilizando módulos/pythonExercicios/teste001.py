from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, ceil(raiz))) #Arredonda a raiz pra cima
print('A raiz de {} é igual a {}'.format(num, floor(raiz))) #Arredonda a raiz pra baixo

