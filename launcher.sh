# launcher.sh

###########################
## start photobooth
###########################

# start python virtual enviroment
source ~/wip/photo-booth/virtualenv/envpi2/bin/activate
# start php server
php -S localhost:8000 ~/wip/photo-booth/www/
# open browser
chromium --kiosk http://localhost:8000

###########################
## /END start photobooth
###########################