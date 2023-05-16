#!./env/bin/python

import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import sys


def get_job_listing(keyword: str) -> list:
    response = ((requests.get(f'https://portal.gupy.io/job-search/term={keyword}')
                         .text))
    soup = BeautifulSoup(response, 'html.parser')

    vagas = []
    list_items = soup.find_all('li')

    for item in list_items:
        vagas.append([item.find('h4').text,
                      item.find_all('p')[-1].text,
                      item.find_all('a')[0]['href']])
    return vagas

def format_to_dataframe(job_list: list) -> str:
    df = pd.DataFrame(job_list, columns=['vaga', 'data', 'url'])
    df['data'] = df['data'].str.replace(r'.*(?<= )', '', regex=True)
    today = dt.datetime.today().strftime('%d/%m/%Y')

    if not df['data'].str.contains(today).any():
        sys.exit('No new jobs today!')

    return df.loc[df['data'] == today, :]
