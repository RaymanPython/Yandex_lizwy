from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def mars():
    return "Миссия Колонизация Марса"


@app.route('/index')
def apple():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return f"Человечество вырастает из детства.</br></br>" \
           f"Человечеству мала одна планета.</br></br>" \
           f"Мы сделаем обитаемыми безжизненные пока планеты.</br></br>" \
           f"И начнем с Марса!</br></br>" \
           f"Присоединяйся!"


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="{url_for('static', filename='img/mars.png')}" alt="альтернативный текст">
                  <body>
                    <br><h>Похожа на колбасу!</h>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
