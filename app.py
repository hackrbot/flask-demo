from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'First App'


@app.route('/name')
def name():
    return 'Rahul Raj'


if __name__ == '__main__':
    app.run()
