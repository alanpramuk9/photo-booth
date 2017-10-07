# pi photobooth
#from picamera import PiCamera
from time import sleep
#from datetime import datetime
import uuid
from PIL import Image
import imageio
import numpy as np

outputPath = './camera-shots/'
#camera = PiCamera()
#id = uuid.uuid4()
# static id for testing
id = '94457bc8-a749-4afc-aa06-11c50bc942c0'
# static image path for testing
imageNames = (
    'photo-0__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    'photo-1__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    'photo-2__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg',
    'photo-3__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg'
    )
overlayImageNames = np.array([])

#camera.start_preview()
sleep(3)
for i in range(4):
    sleep(1)
    #imageName = '/home/pi/wip/photo-booth/camera-shots/photo-'+str(i)+'__'+str(id)+'.jpg'
    imageNameWithOverlay = outputPath+'overlay-photo-'+str(i)+'__'+str(id)+'.jpg'
    print(imageNames[i])
    #camera.capture(imageName)
    # setup overlay images
    background = Image.open(outputPath+imageNames[i])
    foreground = Image.open('./assets/overlay.png')
    # merge photos
    background.paste(foreground, (0, 0), foreground)
    background.save(imageNameWithOverlay)
    overlayImageNames = np.append(overlayImageNames, imageNameWithOverlay)
    print('round '+str(i))
# make gif
print('start making gif')
images = []
for filename in overlayImageNames:
    images.append(imageio.imread(filename))
imageio.mimsave(outputPath+str(id)+'.gif', images)
print('all done')
#camera.stop_preview()
