# launcher.sh

###########################
## start photobooth
###########################

# start python virtual enviroment
cd ~/wip/photo-booth/
source virtualenv/envpi2/bin/activate
# open browser
chromium-browser --kiosk http://localhost

###########################
## /END start photobooth
###########################