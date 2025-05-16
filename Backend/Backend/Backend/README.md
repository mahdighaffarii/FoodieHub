# FoodieHub Backend

Backend API for the FoodieHub application built with Django.

## Features

- Food listing and management
- RESTful API endpoints
- User authentication
- Admin panel for easy management

## Setup

1. Clone the repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create a superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- `/api/foods/` - List all foods
- `/api/foods/<id>/` - Get food details

## Technologies Used

- Django
- SQLite (development)
- Django Admin 