nome = str(input('Qual é o seu nome? ')).strip().upper()

if nome == 'IVONEIDE':
    print('Que nome bonito!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'ANA CLAÚDIA JÉSSICA JULIANA':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem norma.')
print('Tenha um bom dia, {}{}{}'.format('\033[1;35m', nome, '\033[m'))
