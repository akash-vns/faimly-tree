#!/bin/bash
echo "Dumpy data start"
./manage.py dumpdata user auth.user --indent 4 > user/fixtures/dummy_data.json
echo "Dumpy data end"