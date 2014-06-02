#!/bin/sh

apt-get install python-setuptools

sudo easy_install flask
sudo easy_install flask-cors

sudo apt-get install python-gevent
sudo apt-get install gunicorn

git clone https://github.com/migurski/atkinson /tmp/atkinson
cd /tmp/atkinson
sudo python setup.py install
