'''
DESAFIO 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

print('-=' * 15)
print('Índice de Massa Corporal (IMC)')
print('-=' * 15)

peso = float(input('Seu peso: (Kg) '))
altura = float(input('Sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))

if imc < 18.5:
    print('STATUS: Abaixo do peso')
elif 18.5 <= imc < 25:
    print('STATUS: Peso ideal')
elif 25 <= imc < 30:
    print('STATUS: Sobrepeso')
elif 30 <= imc < 40:
    print('STATUS: Obesidade')
elif imc >= 40:
    print('STATUS: Obesidade mórbida')

