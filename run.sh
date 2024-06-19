#!/bin/bash

# Install dependencies
python -m pip install -r requirements.txt

# Run the Django development server
python manage.py runserver
