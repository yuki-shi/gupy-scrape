#!/bin/sh

python3 -m venv env
pip install -r requirements.txt
chmod u+x gupyuki.py main.py
