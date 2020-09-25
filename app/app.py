import logging
import flask
import io

import torchvision
from PIL import Image
from PIL import ImageDraw
from flask import Flask

app = Flask(__name__)
# Confirm file extension is a valid image
app.config['IMAGE_EXTENSIONS'] = ['.jpg', '.png', '.gif']

logging.basicConfig(level=logging.DEBUG)
stdout = app.logger

# TODO: determine where and when to load model into memory with
# setting the correct configuration
# Load pre-trained model into memory
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()
# model.to(device)


@app.route('/')
def index():
    return flask.render_template('index.html')


def verify(content):
    # TODO review and validate the file submission
    # TODO raise exceptions if missing, too much, or wrong data
    # TODO find an easier way to perform stdout
    pass


def extract_image(image_bytes):
    return Image.open(io.BytesIO(image_bytes))


def transform_image(image):
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor()
    ])
    # TODO: place a check here all images are float32
    return transform(image)


def object_detection(tensor):
    out = model([tensor])
    return out[0]


def add_bounding_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    draw.rectangle(detections['boxes'][0].detach().numpy(), outline='red', width=3)
    return draw


@app.route('/', methods=['POST'])
def upload_image():
    content = flask.request.files['image']
    # TODO: verify contents is image
    img_bytes = content.read()
    img = extract_image(img_bytes)
    img_tensor = transform_image(img)
    detections = object_detection(img_tensor)
    result = add_bounding_boxes(img, detections)
    output = io.BytesIO()
    img.convert('RGBA').save(output, format='png')
    output.seek(0, 0)
    return flask.send_file(output, mimetype='image/png', as_attachment=False)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
