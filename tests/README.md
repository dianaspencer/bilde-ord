# Test suite for Bildeord

A quick way to troubleshoot the object detection endpoint
is to use the following command line in the terminal:
```
curl -F "image=@./tests/test_img/living-room.jpg" -i -X POST -H "Content-Type: multipart/form-data" http://127.0.0.1:5000
```
