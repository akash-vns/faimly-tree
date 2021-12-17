#!/bin/bash

echo "Migrating .."
./manage.py migrate


echo "Running server"
./manage.py runserver 8001