from urllib.request import urlopen
from json import loads
import ssl


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

with urlopen('https://danepubliczne.imgw.pl/api/data/synop/') as site:
    alldata = loads(site.read().decode('utf-8'))

data = list(filter(lambda x: x['stacja'] == 'Warszawa', alldata))
print('Stacja: ', data[0]['stacja'])
print('Godzina: ', data[0]['godzina_pomiaru'])
print('Temperatura: ', data[0]['temperatura'])
