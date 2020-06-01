#!/bin/bash

python3.6 -V > /dev/null 2>&1 || {
	echo >&2 "Python 3.6 doesn't seem to be installed! Do you have a weird installation?"
	echo >&2 "If you have python 3.5, use it to run bot.py instead of this script."
	exit 1; }

# Heroku config var handling...
sed "s/Token =/Token = $token/;s/Owner_ID =/Owner_ID = $owner;s/Developer_IDs =/Developer_IDs = $developer" config/config.ini > config/config.ini.new
mv config/config.ini.new config/config.ini

python3.6 app.py
