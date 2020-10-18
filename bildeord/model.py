import io
import os
import torch
import torchvision

from PIL import Image
from PIL import ImageDraw

DEVICE = "cpu"  # FIXME: Collect env var
torch.manual_seed(1234)

# Override default pytorch model_dir
model_dir = os.environ.get('MODEL_DIR')
if not os.path.exists(model_dir):
   os.mkdir(model_dir)
os.environ['TORCH_HOME'] = "./models"  # FIXME: collect env dir

# Download pretrained model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)

# Model only used for evaluation and not training purposes
model.eval()
model.to(DEVICE)


def extract_image(image_bytes):
    return Image.open(io.BytesIO(image_bytes))


def transform_image(image):
    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor()
    ])
    # TODO: place a check here all images are float32
    return transform(image)


def predict(tensor):
    out = model([tensor])
    return out[0]


def add_bounding_boxes(image, detections):
    draw = ImageDraw.Draw(image)
    draw.rectangle(detections['boxes'][0].detach().numpy(), outline='red', width=3)
    return draw


def detection(content):
    img = extract_image(content)
    #img_tensor = transform_image(img)
    #predictions = predict(img_tensor)
    #_ = add_bounding_boxes(img, predictions)
    return img
