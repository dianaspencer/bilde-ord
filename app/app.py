import logging
import flask
import io

import model
from flask import Flask

app = Flask(__name__)
# Confirm file extension is a valid image
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.gif']

logging.basicConfig(level=logging.DEBUG)
stdout = app.logger


@app.route('/')
def index():
    return flask.render_template('index.html')


def verify(content):
    # TODO review and validate the file submission
    # TODO raise exceptions if missing, too much, or wrong data
    # TODO find an easier way to perform stdout
    pass


@app.route('/', methods=['POST'])
def upload_image():
    content = flask.request.files['image']
    # TODO: verify contents is image

    img_bytes = content.read()
    img = model.object_detection(img_bytes)
    output = io.BytesIO()
    img.convert('RGBA').save(output, format='png')
    output.seek(0, 0)
    return flask.send_file(output, mimetype='image/png', as_attachment=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
