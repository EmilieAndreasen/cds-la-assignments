#!/usr/bin/bash

# Check if a script name was provided as an argument
if [ -z "$1" ]; then
    echo "No script specified. Usage: bash run.sh [script_name]"
    exit 1
fi

# Validate the script name
if [ "$1" != "logistic_reg_classifier.py" ] && [ "$1" != "neural_network_classifier.py" ]; then
    echo "Invalid script name. Use either 'logistic_reg_classifier.py' or 'neural_network_classifier.py'"
    exit 1
fi

# Activate the environment
source ./env/bin/activate

# Change directory to the src folder
cd src

# Run the specified Python script
python "$1" "${@:2}"

# Deactivate the environment
deactivate