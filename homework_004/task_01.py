import asyncio
import sys
import time
import aiohttp
import multiprocessing
import threading
import requests


def get_url_thr(url: str):
    response = requests.get(url).content
    with open(f'{url.split("/")[-1]}', "wb") as f:
        f.write(response)


def start_thread(urls: list):
    ts = time.time()
    threads = []
    for i in urls:
        t = threading.Thread(target=get_url_thr, args=i)
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()
    tf = time.time()
    print(f'Время загрузки {tf - ts}')


def get_url_multi(url: str):
    response = requests.get(url).content
    with open(f'{url.split("/")[-1]}', "wb") as f:
        f.write(response)


def start_multiproc(urls: list):
    ts = time.time()
    proces = []
    for i in urls:
        t = multiprocessing.Process(target=get_url_multi, args=i)
        proces.append(t)
        t.start()

    for i in proces:
        i.join()
    tf = time.time()
    print(f'Время загрузки {tf - ts}')


async def get_url_a(url: str):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as resp:
            async with s.get(url) as responce:
                with open(f'{url.split("/")[-1]}', "wb") as f:
                    content = await responce.content.read()
                    f.write(content)


async def main():
    tasks = []
    for url in urls:
        tasks.append(get_url_a(url))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls = sys.argv[1:]
    a = int(input("Выберите как скачать файлы: 1 - Многопоточно, 2 - Многопроцессорно, 3 - Асинхронно :"))
    if a in [1, 2, 3]:
        if a == 3:
            ts = time.time()
            asyncio.run(main())
            tf = time.time()
            print(f'Задача выполнена за {tf - ts}')
        elif a == 1:
            start_thread(urls)
        elif a == 2:
            start_multiproc(urls)
    else:
        print("Внимательней надо было")
