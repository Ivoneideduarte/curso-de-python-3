'''
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}'.format(a, b))
'''

'''
nome = 'Ivoneide'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
'''

nome = 'Ivoneide'
cores = {
         'limpa' : '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'preto_e_branco' : '\033[7;30m'
        }

print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))