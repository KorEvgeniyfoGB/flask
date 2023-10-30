import asyncio
import aiohttp
import time

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        ] * 10


async def get_url(url, n):
    async with aiohttp.ClientSession() as s:
        async with s.get(url) as responce:
            with open(f'asynsfiles/files{n}', "w", encoding="UTF-8") as f:
                txt = await responce.text()
                f.write(txt)


async def main():
    tasks = []
    for n, url in enumerate(urls):
        tasks.append(get_url(url, n))
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    ts = time.time()
    asyncio.run(main())
    tf = time.time()
    print(f'Задача выполнена за {tf - ts}')