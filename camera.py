# pi photobooth
#from picamera import PiCamera
import time
import datetime
import csv
import os
#from datetime import datetime
import uuid
#from PIL import Image
#import imageio
import numpy as np

class Person(object):

    def __init__(self):
        # set id, name, email, zip, age, images, finalImages, gif
        self.id =  uuid.uuid4()
        self.name = "No name"
        self.email = "No email"
        self.age = 0
        self.zipcode = "38305"
        self.images = np.array([])
        self.finalImages = np.array([])
        self.gif = np.array([])

    def load(self):
        # attempt to load last unfinished person
        pass

    def save(self):
        # attempt to save person
        pass

    def destroy(self):
        # attempt to save person
        pass

outputPath = './camera-shots/'
#camera = PiCamera()
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
    person.images = imageNames
    ######
    # take picture
    ######
    # #camera.start_preview()
    # sleep(3)
    # for i in range(4):
    #     sleep(1)
    #     #imageName = '/home/pi/wip/photo-booth/camera-shots/photo-'+str(i)+'__'+str(id)+'.jpg'
    #     imageNameWithOverlay = outputPath+'overlay-photo-'+str(i)+'__'+str(id)+'.jpg'
    #     print(imageNames[i])
    #     #camera.capture(imageName)
    #     # setup overlay images
    #     background = Image.open(outputPath+imageNames[i])
    #     foreground = Image.open('./assets/overlay.png')
    #     # merge photos
    #     background.paste(foreground, (0, 0), foreground)
    #     background.save(imageNameWithOverlay)
    #     overlayImageNames = np.append(overlayImageNames, imageNameWithOverlay)
    #     print('round '+str(i))
    # # make gif
    # print('start making gif')
    # images = []
    # for filename in overlayImageNames:
    #     images.append(imageio.imread(filename))
    # imageio.mimsave(outputPath+str(id)+'.gif', images)
    # print('all done')
    # #camera.stop_preview()
    ######
    # save data to CSV
    ######
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
            print('Time: {0} Name: {1} Email: {2}'.format(reading_time, person.name, person.email))
            writer.writerow([person.id, reading_time, person.name, person.email, person.age, person.zipcode, person.images, person.finalImages, person.gif, False, False])
        os.rename('photoshoots-temp.csv','photoshoots.csv')
    break

# Once the main loop ends (by picking the quit option) save the person state.
person.save()
