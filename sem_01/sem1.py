from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "<p> Hello </p>"


@app.route("/about/")
def about():
    return "<p> About </p>"


@app.route("/contact/")
def con():
    return "<p> Contact </p>"


@app.route("/summ/<int:num1>/<int:num2>")
def summa(num1, num2):
    return f"Сумма  = {num1 + num2}"


students = [
    {"name": "Иван", "surname": "Иванов", "age": 18, "raiting": 3},
    {"name": "Иван1", "surname": "Иванов1", "age": 19, "raiting": 3},
    {"name": "Иван2", "surname": "Иванов2", "age": 18, "raiting": 3},
    {"name": "Иван3", "surname": "Иванов3", "age": 18, "raiting": 3}
]


@app.route("/students")
def get_stud():
    return render_template("students.html", students=students)


news = [
    {"name_news": "dsfgdfgd", "text_news": "gggggggg grgrgrg grsw", "date_news": "12.12.12"},
    {"name_news": "dsfgdfgd1", "text_news": "gggggggg grgrgrg grsw hhgjjhgjh", "date_news": "13.12.12"},
    {"name_news": "dsfgdfgd2", "text_news": "gggggggg grgrgrg grsw wewerytuyiuiu", "date_news": "14.12.12"},
]


@app.route("/news")
def get_news():
    return render_template("news.html", news=news)


if __name__ == "__main__":
    app.run(debug=True)
