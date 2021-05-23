from urllib.request import urlopen
from json import loads
import ssl
from urllib.error import HTTPError, URLError


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

URL = 'https://restcountries.eu/rest/v2/name/'

capitals = {}
while True:
    country = input('\nEnter country name: (E-End) ')
    if country in 'eE':
        break
    if country in capitals.keys():
        print(f'Capital of {country}: {capitals[country]}')
    else:
        try:
            with urlopen(URL + country) as site:
                data = loads(site.read().decode('utf-8'))
                print(f'Capital of {data[0]["name"]}: {data[0]["capital"]}')
                capitals[country] = data[0]["capital"]
        except HTTPError as err:
            if err.code == 404:
                print(f'Country {country}: Not Found')
            else:
                print(err)
        except URLError:
            print('You do not have internet connection!')
