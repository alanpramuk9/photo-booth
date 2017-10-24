# pi photobooth
from picamera import PiCamera
import time
import datetime
import csv
import os
import uuid
from PIL import Image
import imageio
import numpy as np
import sys, json

## globals
outputPath = './camera-shots/'

class Person(object):

    def __init__(self):
        # set id, name, email, zip, age, images, finalImages, gif
        self.id =  uuid.uuid4()
        # self.id = '94457bc8-a749-4afc-aa06-11c50bc942c0'
        self.fname = "No first name"
        self.lname = "No last name"
        self.email = "No email"
        self.age = 0
        self.zipcode = "38305"
        self.images = np.array([])
        self.finalImages = np.array([])
        self.resizeFinalImages = np.array([])
        self.gif = np.array([])

    def load(self):
        # attempt to load last unfinished person
        pass

    def save(self):
        # Create a new photoshoots.csv file that will contain all person data.
        with open('photoshoots.csv') as csv_in_file:
            reader = csv.reader(csv_in_file)
            with open('photoshoots-temp.csv', 'w') as csv_out_file:
                writer = csv.writer(csv_out_file)
                # add ever preexisting row in CSV before adding another
                for row in reader:
                    writer.writerow(row)
                # Write a header row with the name of each column, if the file doesn't exist
                # writer.writerow(['id', 'Time', 'Name', 'Email', 'Age', 'Zipcode', 'Images', 'Final Images', 'Gif', 'Sent', 'Shared'])
                # Now begin writing to the CSV file.
                reading_time = datetime.datetime.now()
                writer.writerow([self.id, reading_time, self.fname, self.lname, self.email, self.age, self.zipcode, self.images, self.finalImages, self.gif, False, False])
            # save to file
            os.rename('photoshoots-temp.csv','photoshoots.csv')
        pass

    def getPhoto(self):
        camera = PiCamera()
        time.sleep(1)
        camera.resolution = (1024, 786)
        camera.start_preview()
        time.sleep(1)
        ## start a countdown
        camera.annotate_text_size = 160
        count = 3
        for x in range(0, 4):
            if count == 0:
                camera.annotate_text = ''
            else:
                camera.annotate_text = str(count)
                time.sleep(1)
            count -= 1
        ## take 4 photos and overlay them each
        for i in range(4):
            time.sleep(1)
            imageName = 'photo-'+str(i)+'__'+str(self.id)+'.jpg'
            imageNameWithOverlay = 'overlay-photo-'+str(i)+'__'+str(self.id)+'.jpg'
            camera.capture(outputPath+imageName)
            self.images = np.append(self.images, imageName)
            # setup overlay images
            background = Image.open(outputPath+self.images[i])
            # background.thumbnail( (500, 500) )
            foreground = Image.open('./assets/camera/overlay.png')
            # merge original jpeg and transparent PNG
            background.paste(foreground, (0, 0), foreground)
            background.save(outputPath+imageNameWithOverlay)
            self.finalImages = np.append(self.finalImages, imageNameWithOverlay)
        # scan complete
        camera.stop_preview()
        # resize
        for i in range(4):
            imageNameOverlayResize = outputPath+'resize-overlay-photo-'+str(i)+'__'+str(self.id)+'.jpg'
            small = Image.open(outputPath+self.finalImages[i])
            small.thumbnail( (500, 500) )
            small.save(imageNameOverlayResize)
            self.resizeFinalImages = np.append(self.resizeFinalImages, imageNameOverlayResize)
        # make gif
        images = []
        count = 0
        for filename in self.resizeFinalImages:
            # add two frames of each photo to gif
            images.append(imageio.imread(filename))
            images.append(imageio.imread(filename))
            count +=1
        self.gif = str(self.id)+'.gif'
        gifPath = outputPath+self.gif
        # saving gif
        imageio.mimsave(gifPath, images)


########
# start the app
########

# Create a person instance and try to load any previous state.
person = Person()
person.load()
person.fname = "Chance"
person.lname = "Smith"
person.email = "test@test.com"
person.age = 31
person.zipcode = 38305

# take photo and save
person.getPhoto()
person.save()

# send back gif file name to index.PHP $result @startphotobooth.php
print(person)