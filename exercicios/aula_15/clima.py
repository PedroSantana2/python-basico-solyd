'''
Crie um porgrama que use de uma API para receber valores de temperatura e clima
'''
import requests
import json
resposta = input('\nDigite o nome da sua cidade: ')
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&appid{Sua chave}&lang=pt_br'.format(resposta))
resultado = json.loads(req.text)
try:
    a = 'Informações de {}:'.format(resultado['name'])
except:
    print('Informação inválida!')
    exit()
print('Informações de {}:'.format(resultado['name']))
print('Paìs: {}'.format(resultado['sys']['country']))
print('Temperatura: {:.1f} °C'.format(float(resultado['main']['temp']) - 273.15))
print('Condição do tempo: {}'.format(resultado['weather'][0]['description']))
