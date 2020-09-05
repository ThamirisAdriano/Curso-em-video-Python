import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('o site Pudim não está acessível no momento')
else:
    print('Consegui aecssar o site Pudim com sucesso.')
    print(site.read())