# launcher.sh

###########################
## start photobooth
###########################

# start python virtual enviroment
cd /home/wip/photo-booth/
source virtualenv/envpi2/bin/activate
# sleep for a bit (5 seconds)
sleep 5
# open browser
chromium-browser --kiosk http://localhost

###########################
## /END start photobooth
###########################