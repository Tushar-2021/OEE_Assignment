# OEE Django Application

## Overview

This Django application calculates and exposes the Overall Equipment Effectiveness (OEE) for machines in a production environment. The application uses a SQLite database to store data about machines and their production logs, computes OEE using the standard formula, and provides a REST API for accessing the OEE data.

## Features

- Models for Machines and Production Logs
- OEE calculation method
- REST API for accessing and filtering OEE data
- Automated tests for models and API endpoints

## Requirements

- Python 3.6+
- Django 3.2+
- Django REST framework
- Django Filter

## Setup Instructions

### Clone the repository

```bash
git clone <YOUR_GITHUB_REPO_URL>
cd oee_project
Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies
bash
Copy code
pip install -r requirements.txt
Apply migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
Run the development server
bash
Copy code
python manage.py runserver
Usage
API Endpoints
Machines API

List all machines: GET /api/machines/
Retrieve a machine: GET /api/machines/{id}/
Create a new machine: POST /api/machines/
Update a machine: PUT /api/machines/{id}/
Delete a machine: DELETE /api/machines/{id}/
Production Logs API

List all production logs: GET /api/production_logs/
Retrieve a production log: GET /api/production_logs/{id}/
Create a new production log: POST /api/production_logs/
Update a production log: PUT /api/production_logs/{id}/
Delete a production log: DELETE /api/production_logs/{id}/
Filtering and Ordering
Filter Machines by machine_name and time
Filter Production Logs by cycle_no, material_name, and machine__machine_name
Order by time for Machines and start_time for Production Logs
