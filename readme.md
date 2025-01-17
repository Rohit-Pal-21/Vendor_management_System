# Vendor Management System API

Welcome to the Vendor Management System API, a Django project for managing vendors, purchase orders, and performance metrics.

## Project Overview

The Vendor Management System provides a set of RESTful APIs for user authentication, vendor management, purchase order creation, and performance metric tracking. It is designed to streamline the process of handling vendors and purchase orders.

## Features

- User Signup and Login
- Vendor Management
- Purchase Order Creation and Management
- Performance Metrics Tracking

## Project Structure

The project structure follows common Django conventions:

- `vendor_management_system/`: Django project directory
  - `Vendor_management_System/`: Django project folder
  - `Vendor/`: Django app containing API views, serializers, and models
  - `manage.py`: Django management script
  - `requirements.txt`: Project dependencies
  - `readme.md`: Project documentation

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Rohit-Pal-21/Vendor_management_System
   ```

2. `cd Vendor-Management-System`
3. `python -m virtualenv`` venv`
4. `for(Windows):venv\Scripts\activate && for(Linux): source venv/bin/activate `
5. `pip install -r requirements.txt`
6. `python manage.py makemigrations`
6. `python manage.py migrate`
7. `python manage.py runserver`

## API Documentation
The API will be accessible at `http://127.0.0.1:8000/`.

API documentation is available `https://www.postman.com/rohitprivate/workspace/fatmug-assignment/request/26297896-24d0972c-8d48-4a91-996b-4c255dcc6428`.

Access the admin interface at `http://127.0.0.1:8000/admin/`.
