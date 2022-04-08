#!/usr/bin/env bash
# exit on error
set -o errexit

clear

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt