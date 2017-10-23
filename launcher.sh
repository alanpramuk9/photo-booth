#!/bin/bash
# launcher.sh

###########################
## start photobooth
###########################

# shopt to add interactive shell
shopt -s expand_aliases
# source the new aliases added
. /home/pi/.bashrc
# start python virtual enviroment (`apb` is an alias  = `. ../.env/bin/activate`)
apb
# open browser (alias = chromium-browser --kiosk http://localhost)
opb

###########################
## /END start photobooth
###########################