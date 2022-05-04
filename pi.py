from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

i = 0 
for i in range(5):
    sleep(2)
    camera.capture(str(i)+'test.jpg') 
    i = i + 1
