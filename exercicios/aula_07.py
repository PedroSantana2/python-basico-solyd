'''
Escreva uma função que recebe um objeto de coleção e retorna o valor do maior número dentro dessa coleção
'''

def maior():
    lista = []
    var = True
    print('Digite SAIR para ter as informações!')
    while var:
        numero = input('Digite um número: ')

        if numero.upper() == 'SAIR':
            var = False

        elif numero.isnumeric():
            lista.append(float(numero))

        else:
            print('Opção invalida!')

    a = sorted(lista)
    return a[-1]
