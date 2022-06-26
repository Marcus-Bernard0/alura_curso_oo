#Verifica se a URL segue o padrão correto
'''
Exemplos de URLs válidas:

bytebank.com/cambio
bytebank.com.br/cambio
www.bytebank.com/cambio
www.bytebank.com.br/cambio
http://www.bytebank.com/cambio
http://www.bytebank.com.br/cambio
https://www.bytebank.com/cambio
https://www.bytebank.com.br/cambio

Exemplos de URLs inválidas:

https://bytebank/cambio
https://bytebank.naoexiste/cambio
ht://bytebank.naoexiste/cambi

'''

#https://www.bytebank.com/cambio
import re

url = 'https://www.bytebank.com/cambio'
padrao_url = re.compile( '(http[s]?://)?(www.)(bytebank.com)(.br)?(/cambio)')
match = padrao_url.match(url)

if not match:
    raise ValueError("A Url não é válida")
print("A URL é valida")