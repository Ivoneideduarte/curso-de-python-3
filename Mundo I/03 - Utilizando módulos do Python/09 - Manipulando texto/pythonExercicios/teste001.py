frase = 'Curso em Vídeo Python'
#Fatiamento
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[::2])

#Análise
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))

#Transformação
#frase = '  Curso em Vídeo Python  '
print(len(frase.strip()))

frase = frase.replace('Python', 'Android')
print(frase)

print('Curso' in frase)

print(frase.lower().find('Curso'))

dividido = frase.split()
print(dividido[2][3])
