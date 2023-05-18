#!/bin/sh

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
chmod u+x gupyuki.py main.py
deactivate
