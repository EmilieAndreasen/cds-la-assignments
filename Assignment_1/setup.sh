#!/usr/bin/bash

# Create virtual environment
python -m venv env

# Activate environment
source ./env/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Install the en_core_web_md model for spaCy
python -m spacy download en_core_web_md

# Deactivate the environment
deactivate
