import time
import os
import asyncio
import aiofiles


async def get_content(filename):
    async with aiofiles.open(filename, "r", encoding='UTF-8') as f:
        content = (await f.read()).split()
    print(f'Количество слов в {filename}: {len(content)}')


async def main():
    tasks = []
    for i in os.listdir('multipcfiles'):
        tasks.append(get_content('multipcfiles/' + i))
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    ts = time.time()
    asyncio.run(main())
    tf = time.time()
    print(f'Время работы {tf - ts}')


