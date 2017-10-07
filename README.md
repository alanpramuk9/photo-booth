# photo-booth
Raspberry Pi Photo booth (PiCamera v2)

## setup
1. begin setup on raspberry pi
1. $`cd virtualenv && virtualenv env --not-site-packages` to prep all dependencies in project
1. start vitural environment in `virtualenv/env/` folder $`source bin/activate` (see: http://sourabhbajaj.com/mac-setup/Python/virtualenv.html)
1. If setting up rPi, be ready to get some coffee. This next step takes a bit to install. (~15mins)
1. go fetch all python dependencies $`cd .. && pip install -r requirements.txt`
1. setup picamera $`sudo apt-get install python3-setuptools && easy_install3 --user picamera` (see: https://media.readthedocs.org/pdf/picamera/release-0.8/picamera.pdf)

## helpful tips with setup
- connect mac to pi file system for editing (see: https://www.raspberrypi.org/documentation/remote-access/ssh/sshfs.md)
- stop virtual environment $`deactivate`
- freeze new dependencies while virtual environment is active (see setup #3) in `virtualenv/env/` folder $`pip freeze --local > requirements.txt`

## virtualenv - virtual enviroment introduction
- docs - http://sourabhbajaj.com/mac-setup/Python/virtualenv.html
- https://www.youtube.com/watch?v=VgP0xzLeLgA
- virtualenv, pip freeze, pip install >> https://www.youtube.com/watch?v=N5vscPTWKOk
- moving to Docker >> https://www.youtube.com/watch?v=ETL-_W1W8gY

## To-Dos
- [X] take picture
- [X] overlay PNG onto pictures taken
- [X] take 4 photos and make a gif
- [ ] collect user data, before taking photo
- [ ] store user data, photo file names, uuid, and if sent/emailed/shared
- [ ] add visual countdown until camera captures photo
- [ ] send/batch social share and/or email the user a copy of photo/gif (see: https://www.raspberrypi.org/learning/tweeting-babbage/worksheet/)
- [ ] remove excess photos?? (9 total assets per instance)
- [ ] add overlay to preview (see: http://picamera.readthedocs.io/en/release-1.10/api_camera.html#picamera.camera.PiCamera.add_overlay)
- [ ] create slideshow of local `./camera-shots/`