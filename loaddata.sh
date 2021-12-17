#!/bin/bash
echo "Load data start"
./manage.py loaddata user/fixtures/*
echo "Load data end"