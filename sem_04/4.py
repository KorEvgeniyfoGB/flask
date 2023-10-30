# Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
import threading
import os
import time
from icecream import ic


def get_content(filename):
    with open(filename, "r", encoding='UTF-8') as f:
        lst_words = f.read().split()
    print(f'Количество слов {len(lst_words)}')


if __name__ == "__main__":
    ts = time.time()
    threads = []
    for file in os.listdir("threadingfiles"):
        t = threading.Thread(target=get_content, args=(f'threadingfiles/{os.path.basename(file)}', ))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    tf = time.time()
    print(f'Время работы {tf - ts}')





