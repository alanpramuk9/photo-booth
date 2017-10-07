# pi photobooth
#from picamera import PiCamera
import time
import datetime
import csv
import os
import uuid
from PIL import Image
import imageio
import numpy as np

## globals
outputPath = './camera-shots/'

class Person(object):

    def __init__(self):
        # set id, name, email, zip, age, images, finalImages, gif
        # self.id =  uuid.uuid4()
        self.id = '94457bc8-a749-4afc-aa06-11c50bc942c0'
        self.name = "No name"
        self.email = "No email"
        self.age = 0
        self.zipcode = "38305"
        self.images = np.array(['photo-0__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg','photo-1__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg','photo-2__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg','photo-3__94457bc8-a749-4afc-aa06-11c50bc942c0.jpg'])
        self.finalImages = np.array([])
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
                # Print out the data and write new row to the CSV file.
                print('Time: {0} Name: {1} Email: {2}'.format(reading_time, self.name, self.email))
                writer.writerow([self.id, reading_time, self.name, self.email, self.age, self.zipcode, self.images, self.finalImages, self.gif, False, False])
            # save to file
            os.rename('photoshoots-temp.csv','photoshoots.csv')
        pass

    def getPhoto(self):
        #camera = PiCamera()
        #camera.start_preview()
        time.sleep(1)
        for i in range(4):
            time.sleep(1)
            #imageName = '/home/pi/wip/photo-booth/camera-shots/photo-'+str(i)+'__'+str(id)+'.jpg'
            imageNameWithOverlay = outputPath+'overlay-photo-'+str(i)+'__'+str(self.id)+'.jpg'
            #camera.capture(imageName)
            # setup overlay images
            background = Image.open(outputPath+self.images[i])
            foreground = Image.open('./assets/overlay.png')
            # merge photos
            background.paste(foreground, (0, 0), foreground)
            background.save(imageNameWithOverlay)
            self.finalImages = np.append(self.finalImages, imageNameWithOverlay)
        # make gif
        print('start making gif')
        images = []
        for filename in self.finalImages:
            images.append(imageio.imread(filename))
        self.gif = str(self.id)+'.gif'
        gifPath = outputPath+self.gif
        imageio.mimsave(gifPath, images)
        print('all done with photoshoot')
        #camera.stop_preview()

########
# start the app
########
# Create a person instance and try to load any previous state.
person = Person()
person.load()
# Now run in a loop and allow the name and color to be changed.
while True:
    ####
    # get data from user
    ####
    person.name = input("Okay, Let's get to know you. What's your name?: ")
    person.age = input("Hey, "+person.name+"! How old are you?: ")
    person.zipcode = input("What's your zipcode?: ")
    person.email = input("What's your email?: ")
    break
# Once the main loop ends (by picking the quit option) save the person state.
person.getPhoto()
person.save()
