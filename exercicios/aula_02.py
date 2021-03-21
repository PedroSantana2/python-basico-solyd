'''
Faça um programa que pergunte o nome, cpf, endereço, idade, altura e telefone de uma pessoa e imprima isso em um relatório organizado.
'''

nome = input('Digite seu nome: ')
cpf = input('Digite seu cpf: ')
endereco = input('Digite seu endereço: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
telefone = input('Digite seu número telefônico: ')
print('''
Relatório
Seu nome: {}
Seu cpf: {}
Seu endereço: {}
Sua idade: {}
Sua altura: {}
Seu telefone: {}
'''.format(nome, cpf, endereco, idade, altura, telefone))
