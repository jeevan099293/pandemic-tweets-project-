#!/bin/bash
# Build script for Render deployment

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Generating visualization data..."
python generate_data.py

echo "Build completed successfully!"
