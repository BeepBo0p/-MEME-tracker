#!/bin/bash
# A script for setting up venv on unix-based systems with bash
python -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt