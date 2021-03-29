'''
Cri um programa que usa uma API para receber a cotação do dólar
'''
import requests
import json


req = requests.get('https://api.hgbrasil.com/finance')
dicionario = json.loads(req.text)

print('1 Dólar = {:.2f} Reais'.format(dicionario['results']['currencies']['USD']['buy']))