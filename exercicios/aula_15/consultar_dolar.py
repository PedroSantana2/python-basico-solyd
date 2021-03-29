'''
Recebendo valor do dólar
'''
import requests
import re
req = requests.get('https://dolarhoje.com/')

resultado = re.search(r'<input type=\"text\" id=\"nacional\" value=\"[\w," =:.;><]+', req.text)
valor = (resultado.group().replace('<input type="text" id="nacional" value=', '')).replace('"', "")
print('Dólar hoje\n1 Dólar = {} Reais'.format(valor))
