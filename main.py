#!./env/bin/python

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--keyword',
                        '-k',
                        type=str,
                        required=True)
    args = parser.parse_args()

    keyword = args.keyword
    response = ((requests.get(f'https://portal.gupy.io/job-search/term={keyword}')
                         .text))
    soup = BeautifulSoup(response, 'html.parser')

    vagas = {}
    list_items = soup.find_all('li')

    for item in list_items:
        vagas[item.find('h4').text] = item.find_all('p')[-1].text

    df = (pd.DataFrame([vagas]).transpose()
                               .reset_index(names='vaga')
                               .rename(columns={0: 'data'}))
    df['data'] = df['data'].str.replace(r'.*(?<= )', '', regex=True)

    print(tabulate(df,
                   headers=['vaga', 'data de publicação'],
                   tablefmt='psql'))
