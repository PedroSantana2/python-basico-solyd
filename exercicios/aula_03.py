'''
Faça um programa que pergunte a idade, o peso e a altura de uma pessoa e decide se ela está apta a ser do exército.
Para entrar no exército é preciso ter mais de 18 anos, pesar mais ou igual a 60 km e medir mais ou igual a 1.70 metros.
'''
idade = int(input('Digite sua idade: ')) 
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
if idade >= 18 and altura >= 1.7 and peso >= 60:
    print('Você pode entrar no exército!')
else:
    print('Você não pode entrar no exército!')
    