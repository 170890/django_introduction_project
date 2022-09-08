#!/bin/bash

echo "Downloading venv ..."
pip install virtualenv

echo "Creating virtualenv ..."
python3 -m venv venv

echo "Enabling venv ..."
source venv/bin/activate

echo "Downloanding project's dependecies ..."
pip install -r requirements.txt