# photo-booth
Raspberry Pi Photo booth (PiCamera v2)

## setup
1. begin setup on raspberry pi
1. add Apache and PHP $`sudo apt-get install apache2 php7.0 php7.0-opcache`
1. clone this repo into $`cd /var/www/html/`
1. **** I'm sure something will go here too ****
1. $`cd virtualenv && virtualenv -p python3 env --no-site-packages` to prep all dependencies in project
1. start vitural environment $`cd ../ && source virtualenv/env/bin/activate` (see: http://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
1. If setting up rPi, be ready to get some coffee. This next step takes a bit to install. (~15mins)
1. go fetch all python dependencies $`pip install -r virtualenv/requirements.txt`
1. setup picamera $`sudo apt-get install python3-setuptools && easy_install3 --user picamera` (see: https://media.readthedocs.org/pdf/picamera/release-0.8/picamera.pdf)

## helpful tips with setup
- connect mac to pi file system for editing (see: https://www.raspberrypi.org/documentation/remote-access/ssh/sshfs.md)
- stop virtual environment $`deactivate`
- freeze new dependencies while virtual environment is active (see setup #3) in `virtualenv/env/` folder $`pip freeze --local > requirements.txt`
- camera interface settings will Disable if camera ribbon isn't plugged into port (Enable again and restart with camera plugged in)

## virtualenv - virtual enviroment introduction
- docs - http://sourabhbajaj.com/mac-setup/Python/virtualenv.html
- https://www.youtube.com/watch?v=VgP0xzLeLgA
- virtualenv, pip freeze, pip install >> https://www.youtube.com/watch?v=N5vscPTWKOk
- moving to Docker >> https://www.youtube.com/watch?v=ETL-_W1W8gY

## To-Dos
- [X] take picture
- [X] overlay PNG onto pictures taken
- [X] take 4 photos and make a gif
- [X] collect user data into CSV, before taking photo
- [X] store user data, photo file names, uuid, and if sent/emailed/shared
- [ ] create loop to start the next person
- [ ] validate data from user
- [ ] logic for if photoshoot.csv doesn't exist or camera module doesn't work
- [ ] add GUI (maybe Tkinter, appJar, or PyQt) (also see: http://appjar.info/ or https://github.com/cztomczak/cefpython)
- [X] add visual countdown until camera captures photo
- [ ] add visual countdown for each photo being taken (when making a gif)
- [X] resize images so gif is smaller in weight (see: http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.capture)
- [ ] show resulting gif after gif created (start photobooth over after 10 seconds)
- [ ] send/batch social share and/or email the user a copy of photo/gif (see: https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/)
- [ ] add overlay to preview (see: http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.add_overlay)
- [ ] remove excess photos?? (9 total assets per instance)
- [ ] create slideshow of local `./camera-shots/`
