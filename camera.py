# pi photobooth
from picamera import PiCamera
from time import sleep
import uuid
import Image

camera = PiCamera()
id = uuid.uuid4()


camera.start_preview()
sleep(3)
for i in range(4):
    sleep(1)
    imageName = '/home/pi/wip/photo-booth/camera-shots/photo-'+str(i)+'__'+str(id)+'.jpg'
    imageNameWithOverlay = '/home/pi/wip/photo-booth/camera-shots/overlay-photo-'+str(i)+'__'+str(id)+'.jpg'
    print(imageName)
    camera.capture(imageName)
    # setup overlay images
    background = Image.open(imageName)
    foreground = Image.open('/home/pi/wip/photo-booth/assets/overlay.png')
    # merge photos
    background.paste(foreground, (0, 0), foreground)
    background.save(imageNameWithOverlay)
camera.stop_preview()
