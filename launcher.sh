#!/bin/bash
# launcher.sh

###########################
## start photobooth
###########################
function start_photo_booth() {
  # source the new aliases added
  . /home/pi/.bashrc
  # start python virtual enviroment (`apb` is an alias  = `. ../.env/bin/activate`)
  apb
  # open browser (alias = chromium-browser --kiosk http://localhost)
  opb
}

# vroom vroom - start function
start_photo_booth
###########################
## /END start photobooth
###########################