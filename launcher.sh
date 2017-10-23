# launcher.sh

###########################
## start photobooth
###########################

# start python virtual enviroment (`apb` is an alias  = `. ../.env/bin/activate`)
apb
# sleep for a bit (5 seconds)
sleep 5
# open browser
chromium-browser --kiosk http://localhost

###########################
## /END start photobooth
###########################