#!/usr/bin/bash

# Create virtual environment
python -m venv env

# Activate environment
source ./env/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Deactivate the environment
deactivate
