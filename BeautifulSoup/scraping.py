import csv
import pandas as pd

import requests
from bs4 import BeautifulSoup

# link for the test:
# https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html
# https://rezka.ag/series/horror/51512-terra-inkognita-2022.html


def get_data(url: str) -> None:

    # 1 - create a file and add column headers
    with open(f'data.csv', 'w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Title',
                'Title in English',
                'Rating (IMDb)',
                'Country',
                'Film Time',
                'Description',
            )
        )

    # 2 - get html
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    }
    url = 'https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html'
    req = requests.get(url, headers=headers)
    src = req.text

    # 3 - extracting data from text
    soup = BeautifulSoup(src, 'lxml')
    title = soup.find('div', class_='b-post__title').text.lstrip()
    title_eng = soup.find('div', class_='b-post__origtitle').text
    rating = soup.find('span', class_='b-post__info_rates imdb').find('span').text
    country = soup.find(text='Страна').next_element.next_element.next.text
    film_time = soup.find('td', {'itemprop': 'duration'}).text
    description = soup.find('div', class_='b-post__description_text').text.lstrip()

    # 4 - adds the received data to the file
    with open(f'data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                title,
                title_eng,
                rating,
                country,
                film_time,
                description,
            )
        )

    # 5 - pandas analysis
    df = pd.read_csv('data.csv')
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_colwidth", 50)
    pd.set_option('display.width', None)
    print(df)


if __name__ == '__main__':
    url = 'https://rezka.ag/series/comedy/2040-kremnievaya-dolina-2014.html'
    get_data(url)
