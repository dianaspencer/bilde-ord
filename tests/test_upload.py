import os
import requests


def test_upload_image():
    test_dir = "./tests/test_img"
    filename = "living-room.jpg"
    file = {
        "image": (os.path.basename(filename), open(os.path.join(test_dir, filename), 'rb'))
    }
    response = requests.post(url='http://localhost:5000', files=file)
    assert response.status_code == 200


def test_invalid_file_extensions():
    file = {
        "image": ("dummy.txt", b"This is a fake", "rb")
    }
    response = requests.post(url='http://localhost:5000', files=file)
    assert response.status_code == 422

    # test cases
    # gimme.bashrc.jpeg
    # gimme.jpeg.bashrc


def test_hello():
    response = requests.get(url='http://localhost:5000/hello')
    assert response.content == b"Hello world!"
