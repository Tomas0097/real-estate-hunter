#!/bin/bash

set -e

cd /opt/real-estate-hunter

# install/upgrade Python packages based on requirements.txt
pip3 install --no-cache-dir -r requirements.txt


# Django server
cd /opt/real-estate-hunter
python3 -u src/manage.py runserver 0.0.0.0:8088
