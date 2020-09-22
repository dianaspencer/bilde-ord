import logging
import flask
import os

from flask import Flask

app = Flask(__name__)
# Confirm file extension is a valid image
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

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
    # img = unverified_data.read()
    filename = unverified_data.filename
    unverified_data.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return flask.redirect(flask.url_for('index'))


@app.route('/uploads')
def display():
    filename = os.listdir(app.config['UPLOAD_PATH'])[0]
    return flask.send_from_directory(app.config['UPLOAD_PATH'], filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
