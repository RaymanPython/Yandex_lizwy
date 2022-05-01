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


@app.route('/promotion_image')
def bootstrap():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Жди нас, Марс!</h1>
                  </body>
                  <img src="{url_for('static', filename='img/mars.png')}" alt="альтернативный текст">
                  <body>
                    <div class="alert alert-dark" role="alert">
                      <strong>Человечество вырастет из детства.</strong>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <strong>Человечеству мала одна планета.</strong>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <strong>Мы сделаем обитаемыми безжизненные пока планеты.</strong>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <strong>И начнём с Марса!</strong>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <strong>Присоединяйся!</strong>
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <div class="form-group">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
                        <h1><p align="center">Анкета претендента</p></h1>
                        <h2><p align="center">на участие в миссии</p></h2>
                        <input class="form-control" type="text" placeholder="Введите фамилию">
                        <input class="form-control" type="text" placeholder="Введите имя">
                    </div>
                  </body>
                </html>"""


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Моё предложение: {planet_name}</h1>
                    <h2>Эта планета близка к Земле;</h2>
                    <div class="alert alert-success" role="alert">
                      <strong>На ней много необходимых ресурсов;</strong>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <strong>На ней есть вода и атмостфера;</strong>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <strong>На ней есть небольшое магнитное поле;</strong>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <strong>Наконец, она просто красива!</strong>
                    </div>
                  </body>
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def next_choice(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      <strong>Поздравляем! Ваш рейтинг после {level} этапа отбора</strong>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <strong>составляет {rating}!</strong>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <strong>Желаем удачи!</strong>
                    </div>
                  </body>
                </html>"""



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')