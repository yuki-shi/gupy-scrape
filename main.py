#!./env/bin/python

from tabulate import tabulate
import argparse
from gupyuki import get_job_listing, format_to_dataframe

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--keyword',
                        '-k',
                        type=str,
                        required=True)
    args = parser.parse_args()
    keyword = args.keyword

    jobs = get_job_listing(keyword)
    df = format_to_dataframe(jobs)

    print(tabulate(df,
                 #headers=['vaga', 'data de publicação'],
                   tablefmt='grid'))
