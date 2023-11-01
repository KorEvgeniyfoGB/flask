# Создать страницу, на которой будет форма для ввода имени и электронной почты,
# при отправке которой будет создан cookie-файл с данными пользователя, а также
# будет произведено перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён
# cookie-файл с данными пользователя и произведено перенаправление на страницу ввода имени и электронной почты.

from flask import Flask, render_template, request, redirect, make_response

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        response = make_response(redirect("/welcome/"))
        response.set_cookie('name', name)
        response.set_cookie('email', email)
        return response

    return render_template('login.html', title="Вход")



@app.route("/welcome/", methods=['GET', 'POST'])
def priv():
    name = request.cookies.get('name')
    email = request.cookies.get('email')
    return render_template('glav.html', title="Приветствие", name=name, email=email)


@app.route('/logout/')
def logout():
    response = make_response(redirect('/'))
    response.delete_cookie('name')
    response.delete_cookie('email')
    return response


if __name__ == '__main__':
    app.run(debug=True)




