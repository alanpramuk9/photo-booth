# photo-booth
Raspberry Pi Photo booth (PiCamera v2)

## setup on rPi
1. begin setup on raspberry pi
1. add Apache and PHP $`sudo apt-get install apache2 php7.0 php7.0-opcache`
1. setup PHP to have default directory be `./www` in this repo (see insturctions below: "Setup Default PHP Directory")
1. **** I'm sure something will go here too ****
1. $`cd virtualenv && virtualenv -p python3 env --no-site-packages` to prep all dependencies in project
1. start vitural environment $`cd ../ && source virtualenv/env/bin/activate` (see: http://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
1. If setting up rPi, be ready to get some coffee. This next step takes a bit to install. (~15mins)
1. go fetch all python dependencies $`pip install -r virtualenv/requirements.txt`
1. setup picamera $`sudo apt-get install python3-setuptools && easy_install3 --user picamera` (see: https://media.readthedocs.org/pdf/picamera/release-0.8/picamera.pdf)

## setup for running/editing/testing
See below about how to automate this
1. $`cd wip/photo-booth/ && source virtualenv/envpi2/bin/activate`
1. $`cd www/ && php -S localhost:8000`
1. open chrome with url: `localhost:8000`

## setup default PHP directory
source: https://stackoverflow.com/a/23175981/3979495
1. edit `apache2.conf` file $`sudo nano /etc/apache2/apache2.conf`
1. edit `<Directory /var/www/html>` to be `<Directory /home/pi/wip/photo-booth/www>`
1. edit `000-default.conf` file $`sudo nano /etc/apache2/sites-avilable/000-default.conf`
1. edit `/var/www/html` to be `/home/pi/wip/photo-booth/www`
1. restart apache $`sudo service apache2 restart`
1. open chrome and go to url: `localhost`

## prepare the auto launch script on rPi
source: http://blog.startingelectronics.com/auto-start-a-desktop-application-on-the-rapberry-pi/
1. create bash alias: `apb`
1. $`echo "alias apb='. /home/pi/wip/photo-booth/virtualenv/envpi2/bin/activate'" >> ~/.bashrc`
1. create bash alias: `opb`
1. $`echo "alias opb='chromium-browser --kiosk http://localhost'" >> ~/.bashrc`
1. $`echo "alias booth='apb && opb'" >> ~/.bashrc`
1. Okay, now let's make it where terminal opens on boot and `booth` get called #magic
1. make directory for startup $`mkdir -p .config/lxsession/LXDE-pi`
1. edit startup $`echo"@lxterminal" >> .config/lxsession/LXDE-pi/autostart`
1. add booth alias to start on terminal load
1. $`echo "booth" >> ~/.bashrc`
1. now try a reboot

## setup on mac for editing files on rPi
- find pi if needed: $`sudo nmap -sP 10.10.1.1/24`
- $`ssh pi@10.10.1.199`
- $`sshfs pi@10.10.1.199:~/wip/photo-booth/ pi`

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
- [X] create loop to start the next person
- [ ] validate data from user
- [ ] logic for if photoshoot.csv doesn't exist or camera module doesn't work
- [X] add GUI (maybe Tkinter, appJar, or PyQt) (also see: http://appjar.info/ or https://github.com/cztomczak/cefpython)
- [X] add visual countdown until camera captures photo
- [ ] add visual countdown for each photo being taken (when making a gif)
- [X] resize images so gif is smaller in weight (see: http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.capture)
- [X] show resulting gif after gif created (start photobooth over after 10 seconds)
- [ ] send/batch social share and/or email the user a copy of photo/gif (see: https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/)
- [ ] add overlay to preview (see: http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.add_overlay)
- [ ] remove excess photos?? (9 total assets per instance)
- [ ] create slideshow of local `./camera-shots/`
