#verifica se o site esta no ar
import urllib

import urllib.request
try:
    url = urllib.request.urlopen("http://www.pudim.com.br")
except:
    print('Deu merda')
else:
    print('deu certo')


