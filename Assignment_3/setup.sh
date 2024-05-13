#!/usr/bin/bash

# create virtual env
python -m venv env
# activate env
source ./env/bin/activate
# install requirements
pip install --upgrade pip
pip install -r requirements.txt

#pip install scipy==1.11.0 #if the code suddenly doesn't work apply this (note to self)

# close the environment
deactivate