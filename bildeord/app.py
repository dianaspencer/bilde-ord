import flask
import io
import logging
import os
import re

from bildeord import model
from bildeord.error import handlers
from flask import Blueprint
from flask import render_template
from flask import current_app

this_app = Blueprint("app", __name__)

logging.basicConfig(level=logging.DEBUG)


@this_app.route('/')
def index():
    return render_template('index.html')


def validate(content):
    # Validate filename
    file_basename = os.path.basename(content.filename)

    file_split = file_basename.split('.')
    if len(file_split) != 2:
        # File may be an empty string or does not
        # obey "filename.extension" convention.
        raise handlers.InvalidFileUpload(
            message="Invalid File Upload.",
            status_code=400
        )

    file_ext = file_split[-1]
    if file_ext not in current_app.config["ALLOWED_FILE_EXTENSIONS"]:
        raise handlers.InvalidFileUpload(
            message="File extension is not allowed.",
            status_code=422
        )


@this_app.route('/', methods=['POST'])
def object_detection():
    # Collect FileStorage object for incoming image file
    content = flask.request.files['image']
    # Verify file is an image
    verified = validate(content)
    # Get bytes from file stream
    img_bytes = verified.read()

    img = model.detection(img_bytes)

    # Create and write processed image to new output file
    output = io.BytesIO()
    img.convert('RGBA').save(output, format='png')
    output.seek(0, 0)

    return flask.send_file(output, mimetype='image/png', as_attachment=False)
