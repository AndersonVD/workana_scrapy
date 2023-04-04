from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas

from tqdm import tqdm
from bs4 import BeautifulSoup

TERMOS = ['python', 'scrapping', 'raspagem', 'coleta', 'api', 'web', 'crawler',
          'webscraping', 'web scraping', 'web scrapping', 'web crawler', 'webcraw']


headers = {
    'authority': "www.workana.com",
    'pragma': "no-cache",
    'cache-control': "no-cache",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'x-requested-with': "XMLHttpRequest",

    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
    'origin': "https://www.workana.com",

}


def main():

    for termo in tqdm(TERMOS):
        print(f'Buscando por {termo}')
        url = f'https://www.workana.com/jobs?language=pt&skills={termo}'
        response = requests.get(url, headers=headers)
        print(f'Termo {termo} encontrado com sucesso!')
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', class_='project-item')
        total = soup.find('p', class_='col-sm-7')
        total_cards = []
        for card in cards:
            try:
                titulo = card.find('h2', class_='h3').span.text
                descricao = card.find(
                    'div', class_='project-details').text
                valor = card.find('span', class_='values').text
                tempo = card.find('h5', class_='date visible-xs').text
            except Exception as e:
                print(e)
                continue
            total_cards.append({
                'titulo': titulo,
                'descricao': descricao,
                'valor': valor,
                'tempo': tempo
            })
        print(total_cards)
        df = pandas.DataFrame(total_cards)
        df.to_csv(f'{termo}.csv', index=False)


if __name__ == '__main__':
    main()
