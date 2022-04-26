from flask import Flask

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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
