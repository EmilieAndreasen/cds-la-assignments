#!/usr/bin/bash

# Activate the environment
source ./env/bin/activate

# Passing required arguments
cd src
python main.py "$@"

# Deactivate the environment
deactivate
