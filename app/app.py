import logging

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
# Confirm file extension is a valid image
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']

logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')


# TODO review and validate the file submission
# TODO raise exceptions if missing, too much, or wrong data
@app.route('/', methods=['POST'])
def upload_image():
    app.logger.info(request.files)  # TODO find an easier way to perform stdout
    raw_image = request.files['image_file']
    print(raw_image)
    return "Done"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
