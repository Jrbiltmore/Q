#!/bin/bash

# Script to install necessary dependencies for the Quantum ML Time Series Project

echo "Updating system packages..."
sudo apt-get update && sudo apt-get upgrade -y

echo "Installing Python3 and pip..."
sudo apt-get install python3 python3-pip -y

echo "Installing virtualenv..."
pip3 install virtualenv

echo "Creating virtual environment..."
virtualenv venv
source venv/bin/activate

echo "Installing project dependencies..."
pip install -r ../requirements.txt

echo "Installing additional quantum computing libraries..."
pip install qiskit pennylane cirq

echo "Installing machine learning libraries..."
pip install numpy pandas scikit-learn tensorflow keras matplotlib seaborn

echo "Installing time series specific libraries..."
pip install statsmodels pmdarima

echo "Dependencies installed successfully."
