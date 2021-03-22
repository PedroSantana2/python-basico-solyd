'''
Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso, o programa irá perguntar o nome de todas as pessoas e colocarnuma lista de convidados.
Após isso, irá imprimir todos os nomes da lista.
'''
quantidade_convidados = int(input('Digite a quantidade de pessoas que serão convidadas para a festa: '))
contador = 1
lista_convidados = []
while contador <= quantidade_convidados:
    nome = input('Digite o nome do {}º convidado: '.format(contador))
    lista_convidados.append(nome)
    contador += 1
print('Convidados:\n{}'.format(lista_convidados))
