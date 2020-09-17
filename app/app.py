from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world'

@app.route('/prediction')
def object_detection():
    pass


if __name__ == '__main__':
    app.run()
