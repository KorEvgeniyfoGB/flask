import multiprocessing
import requests
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ] * 10

def get_url(url, n):
    response = requests.get(url).text
    with open(f'multipcfiles/filesthreading{n}.html', "w", encoding="UTF-8") as f:
        f.write(response)


if __name__ == "__main__":
    ts = time.time()
    proces = []
    for n, url in enumerate(urls):
        t = multiprocessing.Process(target=get_url, args=(url, n))
        proces.append(t)
        t.start()

    for i in proces:
        i.join()
    tf = time.time()
    print(f'Время загрузки {tf - ts}')
