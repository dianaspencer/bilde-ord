import torch
import torchvision

from PIL import Image, ImageDraw

torch.manual_seed(1234)

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

# Load pre-trained model
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
# Set to eval mode
model.eval()
model.to(device)


def prediction(img):
    return model([img])
