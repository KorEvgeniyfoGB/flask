'''
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал),
и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда»,
«Обувь» и «Куртка», используя базовый шаблон.
'''
from flask import Flask, render_template


app = Flask(__name__)


odejda = [{'name_odejda': 'Ветровка', 'text_odejda': 'от ветра', 'date_odejda': 'осень'},
          {'name_odejda': 'Парка', 'text_odejda': 'Для запарки', 'date_odejda': 'Зима'}]
obuv = [{'name_obuv': 'Сандали', 'text_obuv': 'Под носки', 'date_obuv': 'Всесезонки'}]
kurtka = [{'name_kurtka': 'Шуба', 'text_kurtka': 'Из норки', 'date_kurtka': 'Для понта'}]

@app.route('/')
def magazine():
    return render_template('glav.html')


@app.route('/odejda/')
def get_odejda():
    return render_template('odejda.html', odejda=odejda)


@app.route('/obuv/')
def get_obuv():
    return render_template('obuv.html', obuv=obuv)


@app.route('/kurtka/')
def get_kurtka():
    return render_template('kurtka.html', kurtka=kurtka)



if __name__ == '__main__':
    app.run(debug=True)

