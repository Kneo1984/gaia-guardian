# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def fetch_latest_news(query='Cybersecurity'):
    url = f'https://www.google.com/search?q={query}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    headlines = []
    for g in soup.find_all('div', class_='tF2Cxc')[:5]:
        title = g.find('h3').text if g.find('h3') else 'Kein Titel'
        snippet = g.find('span', class_='aCOpRe').text if g.find('span', class_='aCOpRe') else ''
        headlines.append(f'{title}: {snippet}')
    return headlines
