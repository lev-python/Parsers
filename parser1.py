from  bs4 import BeautifulSoup
import requests

def parse():
    URL = 'http://kinobar.cc/online-7/'
    HEADERS ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    response = requests.get(URL, headers = HEADERS)
    soup =  BeautifulSoup(response.content, 'html.parser')
    titles = soup.find('h2', attrs={"class": "zagolovok"})
    items = soup.find('a')
    comps = []


    for item in items:
        comps.append({
            'title': item.find('a')
        })
        for comp in comps:
            print(comp['title'])
parse()