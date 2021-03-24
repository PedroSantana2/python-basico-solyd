'''
Crie um software de gerenciamento bancário 
Esse software poderá ser capaz de criar clientes e contas 
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
'''

from cliente import Cliente
from conta import Conta
from sys import exit

def criar_cliente():
    nome = input('\n\t[ ? ] Digite o nome do cliente. | ')
    cpf = input('\t[ ? ] Digite o cpf do cliente. | ')
    idade = input('\t[ ? ] Digite a idade do cliente. | ')
    cliente_gerado = Cliente(nome, cpf, idade)
    print('\n\t[ / ] Perfil do cliente criado com sucesso!\n')
    return cliente_gerado

def criar_conta(cliente_gerado):
    print('\t[ ! ] Finalizando cadastro do cliente: {}'.format(cliente_gerado.nome))
    saldo = float(input('\n\t[ ? ] Digite a quantidade em reais que a conta terá. | R$'))
    limite = float(input('\t[ ? ] Digite o limite da conta em reais. | R$'))
    conta_cliente = Conta(cliente_criado, saldo, limite)
    print('\n\t[ / ] Conta do cliente criada com sucesso!\n')
    return conta_cliente

def perguntas():
    print('\n\t[ 1 ] Para sacar dinheiro.\n\t[ 2 ] Para depositar dinheiro.\n\t[ 3 ] Para informar o saldo.')
    resposta_pergunta = input('\t=> ')

    if resposta_pergunta == '1':
        quantidade_sacar = float(input('\n\tDigite a quantidade do saque em reais. | R$'))
        resultado_sacar = conta_cliente.sacar(quantidade_sacar, conta_cliente.saldo, conta_cliente.limite)

    elif resposta_pergunta == '2':
        quantidade_deposito = float(input('\n\tDigite a quantidade do deposito em reais. | R$'))
        resultado_deposito = conta_cliente.depositar(quantidade_deposito)
    
    elif resposta_pergunta == '3':
        conta_cliente.consultar()


mensagem = '=-' * 8 + '$' * 3 + '=-' * 8
print('\n\t{}'.format(mensagem))

verificador = True
while verificador:
    print('\t[ 1 ] Para criar uma conta no banco!\n\t[ 2 ] Para sair do programa!')
    reposta = input('\t=> ')

    if reposta == '1':
        cliente_criado = criar_cliente()
        conta_cliente = criar_conta(cliente_criado)
        verificador = False

    elif reposta == '2':
        exit()

    else:
        print('\n\t[ ! ] Resposta ínvalida, tente novamente!\n')

verificador = True
while verificador:
    print('\t[ 1 ] Para alterar valores da conta.\n\t[ 2 ] Para sair do programa.')
    reposta = input('\t=> ')  
    if reposta == '1':
        perguntas()

    elif reposta == '2':
        exit()

    else:
        print('\n\t[ ! ] Resposta ínvalida, tente novamente!\n')
