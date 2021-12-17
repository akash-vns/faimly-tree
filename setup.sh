#!/bin/bash
echo "Initial Start"

echo "Creating venv"
pip install virtualenv
rm -rf venv
python3 -m virtualenv venv
chmod 755 venv/bin/activate

echo "Activate venv"
. venv/bin/activate
clear
echo "Installing requirements .."
pip install -r requirements.txt
clear
echo "Migrating .."
./manage.py migrate
clear
sh ./loaddata.sh