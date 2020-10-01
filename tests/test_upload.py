import io
import requests


def test_upload_image_stream():
    file_path = "./tests/test_img/living-room.jpg"
    data = {"image": open(file_path, 'rb')}
    response = requests.post(url='http://localhost/test:5000', data=data)
    print(response)
