from flask import Flask, render_template, request
from login import check_credentials

app = Flask(__name__)
# Имя файла, где хранится имя пользователя и пароль
FILE = 'credentials.txt'


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/')
def form():
    # Получение данных формы
    username = request.form.get('username')
    password = request.form.get('password')
    # Проверка на соответствие данным из файла
    if check_credentials(username, password, FILE):
        # Если соответствует - выдаём страницу успешного входа
        return render_template('success.html')
    else:
        # Если нет - возвращаем страницу авторизацией с сообщением о неправильности данных
        return render_template('index.html', isInvalid=True)


if __name__ == '__main__':
    app.run()
