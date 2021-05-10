#!/bin/bash
rm -rf env
python3 -m venv env
. env/bin/activate
pip install --upgrade pip
pip3 install flask
pip3 install firebase-admin
pip3 install humanize