from urllib.request import urlopen
from json import loads

with urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))
    rates = data[0]['rates']
    # print(data[0]['rates'])
value, currency = input('Jaką wartość i w jakiej walucie chcesz wymienić na złotówki? ').split()

# sposób 1
# for cur in rates:
#     if cur['code'] == currency:
#         print(f"Otrzymujesz {cur['mid'] * float(value):.2f} PLN")

# sposób 2
rate = list(filter(lambda x: x['code'] == currency, rates))
print(f"Otrzymujesz {rate[0]['mid'] * float(value):.2f}")
