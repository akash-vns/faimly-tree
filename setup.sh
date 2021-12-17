#!/bin/bash
echo "Initial Start"

echo "Creating venv"
pip install virtualenv
rm -rf venv
python3 -m virtualenv venv
chmod 755 venv/bin/activate

echo "Activate venv"
. venv/bin/activate

echo "Installing requirements .."
pip install -r requirements.txt

echo "Migrating .."
./manage.py migrate
