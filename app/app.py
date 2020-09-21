import logging
import flask

from flask import Flask

app = Flask(__name__)
# Confirm file extension is a valid image
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.gif']

logging.basicConfig(level=logging.DEBUG)
stdout = app.logger


@app.route('/')
def index():
    return flask.render_template('index.html')


# TODO review and validate the file submission
# TODO raise exceptions if missing, too much, or wrong data
# TODO find an easier way to perform stdout
@app.route('/', methods=['POST'])
def upload():
    unverified_data = flask.request.files['image']
    # file_name, file_ext = unverified_data.filename.split('.')
    # if len(file_name) == '' or file_ext not in app.config['IMAGE_EXTENSIONS']:
    #    abort(400)
    img = unverified_data.read()
    return flask.redirect(flask.url_for('index'))


@app.route('/')
def render():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
