import flask
import io
import logging

from bildeord import model
from flask import Blueprint
from flask import render_template
from flask import current_app as ca
from flask import jsonify

bp = Blueprint("app", __name__)

logging.basicConfig(level=logging.DEBUG)


@bp.route('/')
def index():
    return render_template('index.html')


def verify(content):
    allowed_ext = ca.config["ALLOWED_IMAGE_EXTENSIONS"]

    if content.filename == "":
        return "Does not have file name"
    extension = content.filename[:-4]
    if extension not in allowed_ext:
        return "Does not have allowed extension"


@bp.route('/', methods=['POST'])
def object_detection():
    # Collect FileStorage object for incoming image file
    content = flask.request.files['image']
    # Verify file is an image
    verified = verify(content)
    # Get bytes from file stream
    img_bytes = content.read()

    img = model.detection(img_bytes)

    # Create and write processed image to new output file
    output = io.BytesIO()
    img.convert('RGBA').save(output, format='png')
    output.seek(0, 0)

    return flask.send_file(output, mimetype='image/png', as_attachment=False)
