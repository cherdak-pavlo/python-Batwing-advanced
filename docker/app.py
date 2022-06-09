from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    return 'Welcome dear Pavlo!'


@app.route('/hello')
def hello():
    return 'Hello my friend\n' * 50


@app.route('/hy')
def hy():
    return 'Hy-hy-hy\n' * 50


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
