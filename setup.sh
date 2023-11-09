#!/bin/bash

# This script assumes that Python3 and virtualenv are already installed on the system.

# Define the environment name
ENV_NAME="SML_EPI_23"

# Create a virtual environment
virtualenv -p python3 $ENV_NAME

# Activate the virtual environment
source $ENV_NAME/bin/activate

# Upgrade pip to the latest version
pip install --upgrade pip

# Install requirements from requirements.txt
pip install -r requirements.txt

echo "Setup completed. Environment '$ENV_NAME' is ready to use."
echo "Activate it using the command: source $ENV_NAME/bin/activate"
