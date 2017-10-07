# pi photobooth
#from picamera import PiCamera
from time import sleep
from datetime import datetime
import uuid
from PIL import Image

#camera = PiCamera()
#id = uuid.uuid4()
# static id for testing
id = '94457bc8-a749-4afc-aa06-11c50bc942c0'
# static image path for testing
imageName = (
    '/home/pi/wip/photo-booth/camera-shots/photo-0__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    '/home/pi/wip/photo-booth/camera-shots/photo-1__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    '/home/pi/wip/photo-booth/camera-shots/photo-2__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    '/home/pi/wip/photo-booth/camera-shots/photo-3__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg'
    )

#camera.start_preview()
sleep(3)
for i in range(4):
    sleep(1)
    #imageName = '/home/pi/wip/photo-booth/camera-shots/photo-'+str(i)+'__'+str(id)+'.jpg'
    imageNameWithOverlay = '/home/pi/wip/photo-booth/camera-shots/overlay-photo-'+str(i)+'__'+str(id)+'.jpg'
    print(imageName[i])
    #camera.capture(imageName)
    # setup overlay images
    background = Image.open(imageName[i])
    foreground = Image.open('/home/pi/wip/photo-booth/assets/overlay.png')
    # merge photos
    background.paste(foreground, (0, 0), foreground)
    background.save(imageNameWithOverlay)
    # make gif
    print('round '+str(i))
print('all done')
#camera.stop_preview()
