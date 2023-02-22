import requests


def get_downloads(start_date: str, end_date: str):
    url = 'https://api.npmjs.org/downloads/range/{}:{}/lodash'.format(start_date, end_date)
    response = requests.get(url)
    data = response.json()
    download_count = 0

    for download_data in data['downloads']:
        download_count += download_data['downloads']
    return download_count


print(get_downloads('2023-01-01', '2023-01-30'))