__autor_ = 'Vhernandez'
import requests
from bs4 import BeautifulSoup

request = requests.get("https://articulo.mercadolibre.com.mx/MLM-564407651-10-pzs-bolso-mochila-militar-pcelular-sistema-molle-mayoreo-_JM?quantity=1&variation=32550037700#c_id=/home/collections/item&c_campaign=exploradores&c_uid=363cf152-22f8-4ee6-8911-3b38e174286b")
content = request.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find("span", {"class": "price-tag-fraction"})
string_price = element.text.strip()
string_price = string_price.replace(',', '')

price = float(string_price)

if price < 1000:
    print('Muy barato {}'.format(price))
else:
    print('Bien caro ALV {}'.format(price))
